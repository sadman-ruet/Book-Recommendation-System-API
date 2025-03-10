import os
# Load environment variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Environment Variables
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Embeddings & LLM Configuration
EMBEDDINGS_MODEL = "models/text-embedding-004"
LLM_MODEL = "gemini-2.0-flash-lite"
LLM_TEMPERATURE = 0.3
LLM_MAX_TOKENS = 768

# Pinecone Index Name
INDEX_NAME = "book-recommendation-system"
