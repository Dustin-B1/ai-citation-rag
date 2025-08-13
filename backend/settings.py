import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
EMBED_MODEL = os.getenv('EMBEDDINGS_MODEL','text-embedding-3-large')
LLM_MODEL = os.getenv('LLM_MODEL','gpt-5')
DATA_DIR = 'data'
RAW_DIR = f'{DATA_DIR}/raw'
PROC_DIR = f'{DATA_DIR}/processed'
INDEX_DIR = f'{DATA_DIR}/index'
