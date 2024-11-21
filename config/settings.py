import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI API Settings
OPENAI_API_KEY = os.getenv("OA_API")
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
if not OPENAI_API_KEY:
    print("OpenAI API key not found. Please check your environment settings.")

# Model Settings
LLM_MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.5

# File Paths
DATA_PATH = "data/product_processed.csv"
EMBEDDINGS_PATH = "data/embeddings.npz"
FAISS_INDEX_PATH = "data/faiss_index"

# Gradio Settings
GRADIO_SETTINGS = {
    "title": "E-commerce Chatbot",
    "theme": "default",
    "height": 500
}

# Logging Settings
LOG_LEVEL = "INFO"