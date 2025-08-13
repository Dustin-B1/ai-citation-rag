# AI Citation RAG

A simple Retrieval-Augmented Generation (RAG) system with citation support. Upload your documents (PDF, TXT, Markdown, DOCX), query them in natural language, and get answers with relevant citations.  

---

## **Features**
- FastAPI backend with FAISS vector search  
- Streamlit UI for easy interaction  
- PDF, TXT, MD, and DOCX ingestion  
- Retrieves text chunks with scores and source metadata  
- OpenAI API integration for natural language answers  

---

## **Quickstart**

```bash
# 1. Clone the repo
git clone https://github.com/Dustin-B1/ai-citation-rag.git
cd ai-citation-rag

# 2. Create and activate virtual environment (Windows)
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy env template and set your OpenAI key
copy .env.example .env

# 5. Run backend (Terminal 1)
uvicorn backend.app:app --reload

# 6. Run frontend (Terminal 2)
streamlit run ui/streamlit_app.py

Requirements
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
    python-multipart
    Environment Variables
    
    Your .env file should contain:
        OPENAI_API_KEY=your_openai_api_key_here

Usage
   
    Start the backend
        uvicorn backend.app:app --reload
   
   Start the frontend
        streamlit run ui/streamlit_app.py
    
    Ingest Documents
        Go to the sidebar in the Streamlit app
        Upload PDFs, TXT, MD, or DOCX files
        Click “Send to backend”

    Ask Questions
        Type your question in the text input
        Click “Search”
        View the AI-generated answer and retrieved chunks with citations

Project Structure
    ai-citation-rag/
    │── backend/
    │   ├── app.py
    │   ├── ingest.py
    │   ├── query.py
    │── ui/
    │   ├── streamlit_app.py
    │── .env.example
    │── requirements.txt
    │── README.md
Notes
        You must run both backend and frontend simultaneously in separate terminals.
        Works best with clear, well-structured source documents.
        This is a local-first setup — no hosted dependencies beyond OpenAI API.