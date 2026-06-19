import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class FeedbackVectorStore:
    """Stores and searches feedback using ChromaDB embeddings."""
    
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.collection = None
        self._init_collection()
    
    def _init_collection(self):
        try:
            self.collection = self.vector_store.client.get_or_create_collection(
                name="query_feedback",
                metadata={"description": "Verified query/SQL pairs from user feedback"}
            )
            logger.info(f"Feedback collection ready: {self.collection.count()} entries")
        except Exception as e:
            logger.error(f"Failed to init feedback collection: {e}")
            self.collection = None
    
    def add_feedback(self, query: str, sql: str, feedback_id: int):
        """Store a positively rated query/SQL pair with its embedding."""
        if not self.collection:
            return False
        try:
            embedding = self.vector_store.embeddings_client.embed(query)
            self.collection.upsert(
                ids=[str(feedback_id)],
                embeddings=[embedding],
                documents=[query],
                metadatas=[{"sql": sql, "query": query}]
            )
            logger.info(f"Stored feedback embedding for: {query[:50]}")
            return True
        except Exception as e:
            logger.error(f"Failed to store feedback embedding: {e}")
            return False
    
    def find_similar(self, query: str, n_results: int = 3) -> List[Dict]:
        """Find verified query/SQL pairs similar to the given query."""
        if not self.collection or self.collection.count() == 0:
            return []
        try:
            embedding = self.vector_store.embeddings_client.embed(query)
            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=min(n_results, self.collection.count()),
                include=["metadatas", "distances"]
            )
            similar = []
            for meta, distance in zip(
                results["metadatas"][0],
                results["distances"][0]
            ):
                if distance < 0.4:
                    similar.append({
                        "query": meta["query"],
                        "sql": meta["sql"],
                        "similarity": round(1 - distance, 2)
                    })
            logger.info(f"Found {len(similar)} similar feedback entries")
            return similar
        except Exception as e:
            logger.error(f"Feedback similarity search failed: {e}")
            return []
    
    def count(self) -> int:
        if not self.collection:
            return 0
        return self.collection.count()