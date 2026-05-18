"""OpenAI embeddings wrapper for SQL documentation."""

from typing import List, Callable, Any
import os
import re
import openai
from tenacity import retry, stop_after_attempt, wait_exponential

class OpenAIEmbeddingsClient:
    """Handles embeddings generation with error handling and batching."""
    
    def __init__(self):
        api_key = os.getenv("EMBEDDING_API_KEY") or os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("EMBEDDING_API_BASE") or os.getenv("OPENAI_API_BASE")
        self.model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
        self.batch_size = int(os.getenv("EMBEDDING_BATCH_SIZE", "100"))
        self.max_retries = int(os.getenv("EMBEDDING_MAX_RETRIES", "3"))
        
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def generate_embedding(self, text: str) -> List[float]:
        """Generate single embedding for text."""
        prepared_text = self._prepare_text_for_embedding(text)
        response = self.client.embeddings.create(
            input=prepared_text,
            model=self.model
        )
        return response.data[0].embedding

    def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts efficiently."""
        prepared_texts = [self._prepare_text_for_embedding(text) for text in texts]
        embeddings = []
        
        for i in range(0, len(prepared_texts), self.batch_size):
            batch = prepared_texts[i:i + self.batch_size]
            response = self._retry_with_backoff(
                self.client.embeddings.create,
                input=batch,
                model=self.model
            )
            batch_embeddings = [data.embedding for data in response.data]
            embeddings.extend(batch_embeddings)
        
        return embeddings

    def _prepare_text_for_embedding(self, text: str) -> str:
        """Clean and prepare text for embedding generation."""
        text = re.sub(r'\s+', ' ', text.strip())
        # Simple character-based truncation instead of tiktoken
        # nomic-embed-text supports up to ~8000 tokens ~ 32000 chars
        if len(text) > 30000:
            text = text[:30000]
        return text

    def _retry_with_backoff(self, func: Callable, *args: Any, **kwargs: Any) -> Any:
        """Retry failed requests with exponential backoff."""
        @retry(
            stop=stop_after_attempt(self.max_retries),
            wait=wait_exponential(multiplier=1, min=4, max=10)
        )
        def _wrapped_func():
            return func(*args, **kwargs)
            
        return _wrapped_func()