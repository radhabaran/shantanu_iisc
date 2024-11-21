from openai import OpenAI
import numpy as np
import faiss
from config.settings import EMBEDDINGS_PATH, FAISS_INDEX_PATH, OPENAI_API_KEY
from config.prompts import PRODUCT_QUERY_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def load_faiss_index_and_embeddings():
    try:
        index = faiss.read_index(FAISS_INDEX_PATH)
        embeddings_data = np.load(EMBEDDINGS_PATH)
        embeddings = embeddings_data["embeddings"]
        return index, embeddings
    except Exception as e:
        print(f"Error loading FAISS index and embeddings: {e}")
        return None, None

def query_product_info(query: str, index, embeddings):
    try:
        response = client.embeddings.create(
            input=[query],
            model="text-embedding-ada-002"
        )
        query_embedding = response.data[0].embedding
        query_embedding_np = np.array(query_embedding, dtype='float32')
        
        _, indices = index.search(np.array([query_embedding_np]), k=3)
        retrieved_products = [embeddings[i] for i in indices[0]]
        context = "\n\n".join(retrieved_products)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an intelligent assistant for an e-commerce platform."},
                {"role": "user", "content": PRODUCT_QUERY_PROMPT.format(context=context, query=query)}
            ],
            max_tokens=150,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error processing query: {e}"

def handle_product_query(query: str) -> str:
    index, embeddings = load_faiss_index_and_embeddings()
    if index is None or embeddings is None:
        return "Sorry, I'm having trouble accessing the product database."
    return query_product_info(query, index, embeddings)
