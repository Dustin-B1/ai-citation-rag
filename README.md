# AI Citation RAG
Local-first AI document search with hybrid retrieval, span-accurate citations, and an eval harness.

## Quickstart
`ash
python -m venv .venv && .\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn backend.app:app --reload
streamlit run ui/streamlit_app.py

Set-Content requirements.txt @"
fastapi[all]
uvicorn[standard]
python-dotenv
pymupdf
pytesseract
pillow
faiss-cpu
rank-bm25
numpy
pandas
scikit-learn
tiktoken
openai
streamlit
PyYAML
