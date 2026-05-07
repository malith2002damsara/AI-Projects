import re
from typing import List, Optional


class ChatPromptTemplate:
    def __init__(self, template: str, input_variables: Optional[List[str]] = None):
        self.template = template
        self.input_variables = input_variables or list(set(re.findall(r'\{([^{}]+)\}', template)))

    def format(self, **kwargs) -> str:
        missing = [v for v in self.input_variables if v not in kwargs]
        if missing:
            raise ValueError(f"Missing variables: {missing}")
        return self.template.format(**kwargs)


RAG_TEMPLATE = """
Answer the question in a very detailed manner.
Write a comprehensive explanation with multiple paragraphs,
examples, and bullet points.

Question: {question}

Research Context (from multiple papers):
{context}

Instructions for your answer:
1. Provide a comprehensive, detailed response
2. Structure your answer with:
   - Clear headings where appropriate
   - Bullet points for key facts and lists
   - Numbered steps for procedures
   - Detailed paragraphs for explanations
3. When referencing information, note the source paper
4. Be thorough and include all relevant details from the context
5. Use tables if comparing data or listing structured information
6. Format your response in a clear, academic style

Answer:"""


def get_prompt_template() -> ChatPromptTemplate:
    return ChatPromptTemplate(RAG_TEMPLATE)