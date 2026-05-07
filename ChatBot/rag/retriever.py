from typing import List, Dict, Any, Optional


class Retriever:
    def __init__(self, vectorstore, search_type: str = "similarity", search_kwargs: Optional[Dict] = None):
        self.vectorstore = vectorstore
        self.search_type = search_type
        self.search_kwargs = search_kwargs or {"k": 4}

    def get_relevant_documents(self, query: str, **kwargs) -> List[Dict]:
        search_kwargs = {**self.search_kwargs, **kwargs}
        k = search_kwargs.get('k', 4)
        filter_meta = search_kwargs.get('filter')
        return self.vectorstore.similarity_search(query, k=k, filter_metadata=filter_meta)

    def __call__(self, query: str, **kwargs) -> List[Dict]:
        return self.get_relevant_documents(query, **kwargs)