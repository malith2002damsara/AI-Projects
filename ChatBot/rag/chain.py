from typing import Any, Dict, List
from logger import setup_logger

logger = setup_logger(__name__)


def _extract_question(input_data: Any) -> str:
    """Extract question string from various input formats"""
    if isinstance(input_data, str):
        return input_data
    return str(input_data)


def _build_context_string(context_docs: Any) -> tuple[str, List[Dict]]:
    """
    Build formatted context string and extract source information
    
    Returns:
        tuple: (context_string, source_documents)
    """
    context_parts = []
    source_documents = []
    
    # Normalize to list
    docs_list = context_docs if isinstance(context_docs, list) else [context_docs]
    
    for i, doc in enumerate(docs_list, 1):
        if isinstance(doc, dict):
            content = doc.get('page_content', str(doc))
            metadata = doc.get('metadata', {})
            
            source_info = {
                'filename': metadata.get('filename', 'Unknown Source'),
                'page': metadata.get('page', 'N/A'),
                'source_path': metadata.get('source', '')
            }
            
            source_documents.append(source_info)
            source_label = f"[Source {i}: {source_info['filename']}, Page {source_info['page']}]"
            context_parts.append(f"{source_label}\n{content}")
        else:
            content = str(doc)
            context_parts.append(f"[Source {i}]\n{content}")
            source_documents.append({
                'filename': 'Unknown',
                'page': 'N/A',
                'source_path': ''
            })
    
    context = "\n\n---\n\n".join(context_parts)
    return context, source_documents


def _extract_generated_text(llm_output: Any) -> str:
    """Extract text from various LLM output formats"""
    if isinstance(llm_output, list) and llm_output:
        first_item = llm_output[0]
        if isinstance(first_item, dict):
            return first_item.get('generated_text', str(first_item))
        return str(first_item)
    
    if isinstance(llm_output, dict):
        return llm_output.get('generated_text', str(llm_output))
    
    return str(llm_output)


def create_chain(retriever, prompt_template, llm, output_parser):
    """
    Create a RAG chain that retrieves context and generates answers
    
    Args:
        retriever: Document retriever function
        prompt_template: Prompt template with .format() method
        llm: Language model callable
        output_parser: Output parser with .parse() method or callable
    
    Returns:
        Callable chain function
    """
    def chain(input_data: Any) -> Dict:
        """Execute the RAG chain"""
        try:
            # Step 1: Extract question
            question = _extract_question(input_data)
            logger.debug(f"Processing question: {question[:100]}...")

            # Step 2: Retrieve relevant documents
            context_docs = retriever(question)
            logger.debug(f"Retrieved {len(context_docs) if isinstance(context_docs, list) else 1} documents")

            # Step 3: Build context string with source labels
            context, source_documents = _build_context_string(context_docs)

            # Step 4: Format prompt
            formatted_prompt = prompt_template.format(
                question=question,
                context=context
            )

            # Step 5: Run LLM
            logger.debug("Generating response from LLM...")
            llm_output = llm(formatted_prompt) if callable(llm) else llm.invoke(formatted_prompt)

            # Step 6: Extract generated text
            generated_text = _extract_generated_text(llm_output)

            # Step 7: Parse output
            if hasattr(output_parser, 'parse'):
                parsed = output_parser.parse(generated_text)
            else:
                parsed = output_parser(generated_text)
            
            # Step 8: Add metadata
            parsed['source_documents'] = source_documents
            parsed['question'] = question
            
            logger.info("✅ Chain execution completed successfully")
            return parsed
            
        except Exception as e:
            logger.error(f"Chain execution failed: {e}")
            return {
                "answer": f"Error processing request: {str(e)}",
                "question": input_data if isinstance(input_data, str) else str(input_data),
                "source_documents": [],
                "error": str(e)
            }

    return chain