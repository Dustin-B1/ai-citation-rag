import streamlit as st, requests
st.set_page_config(page_title='AI Citation RAG')
st.title('AI Citation RAG')
try:
    ok = requests.get('http://localhost:8000/health', timeout=1).json().get('ok', False)
    st.success('Backend OK' if ok else 'Backend not responding')
except Exception:
    st.warning('Start backend:  uvicorn backend.app:app --reload')
