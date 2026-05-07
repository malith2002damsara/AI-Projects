import re
from collections import defaultdict
from typing import Dict, Any


class TextOutputParser:
    def parse(self, text: str) -> Dict[str, str]:
        answer_match = re.search(r'Answer:\s*(.*)', text, re.DOTALL | re.IGNORECASE)
        if answer_match:
            answer_text = answer_match.group(1).strip()
        else:
            lines = text.split('\n')
            answer_lines = []
            found_answer = False
            for line in lines:
                if 'answer' in line.lower() and ':' in line:
                    found_answer = True
                    continue
                if found_answer or (not any(kw in line.lower() for kw in ['context:', 'question:', 'instructions:'])):
                    answer_lines.append(line)
            answer_text = '\n'.join(answer_lines).strip()
        return {"answer": answer_text if answer_text else text}


def extract_answer(response_data: Any) -> str:
    if isinstance(response_data, dict):
        if 'answer' in response_data:
            return response_data['answer']
        if 'raw_text' in response_data:
            return response_data['raw_text']
    return str(response_data)


def format_output(text: str) -> str:
    lines = text.split('\n')
    formatted_lines = []
    for line in lines:
        if line.strip().startswith(('-', '*', '•', '|')) or re.match(r'^\d+[\.\)]\s', line.strip()):
            formatted_lines.append(line.rstrip())
        elif re.match(r'^[\s\|\-\+\=]+$', line.strip()):
            formatted_lines.append(line.rstrip())
        elif line.strip():
            formatted_lines.append(line.strip())
        elif formatted_lines and formatted_lines[-1] != '':
            formatted_lines.append('')
    return '\n'.join(formatted_lines)


def print_sources(source_documents):
    if not source_documents:
        return
    papers = defaultdict(list)
    for source in source_documents:
        filename = source.get('filename', 'Unknown')
        page = source.get('page', 'N/A')
        papers[filename].append(page)

    print("\n" + "─"*80)
    print("📚 SOURCES / REFERENCES")
    print("─"*80)
    for i, (paper, pages) in enumerate(papers.items(), 1):
        unique_pages = sorted(set(str(p) for p in pages if p != 'N/A'))
        pages_str = f"Pages: {', '.join(unique_pages)}" if unique_pages else "Page info not available"
        print(f"\n[{i}] {paper}")
        print(f"    {pages_str}")
    print("\n" + "─"*80)


def print_answer(response_data: Any, show_metadata: bool = True):
    answer = extract_answer(response_data)
    formatted_answer = format_output(answer)

    print("\n" + "═"*80)
    print("🔍 RAG RESEARCH ANSWER (Local Models)")
    print("═"*80)

    if isinstance(response_data, dict) and 'question' in response_data:
        print(f"\n📝 Question: {response_data['question']}")
        print("\n" + "─"*80)

    print("\n💡 DETAILED ANSWER:\n")
    print(formatted_answer)
    print("\n" + "═"*80)

    if isinstance(response_data, dict) and 'source_documents' in response_data:
        print_sources(response_data['source_documents'])

    if show_metadata and isinstance(response_data, dict):
        print("\n📊 Metadata:")
        print(f"  • Answer length: {len(answer)} characters")
        if 'source_documents' in response_data:
            num_sources = len(response_data['source_documents'])
            num_papers = len(set(s.get('filename', 'Unknown') for s in response_data['source_documents']))
            print(f"  • Source chunks: {num_sources}")
            print(f"  • Unique papers: {num_papers}")
        print("  • Models: Phi-2 (LLM) + all-MiniLM-L6-v2 (Embeddings)")
        print("═"*80 + "\n")