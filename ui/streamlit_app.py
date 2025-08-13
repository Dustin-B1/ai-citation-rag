import streamlit as st, requests

st.set_page_config(page_title='AI Citation RAG', layout='wide')
st.title('AI Citation RAG')
BACKEND = 'http://127.0.0.1:8000'

# Health check
try:
    r = requests.get(f'{BACKEND}/health', timeout=3)
    ok = r.ok and r.json().get('ok', False)
    st.success('Backend OK') if ok else st.error('Backend not responding')
except Exception as e:
    st.error(f'Backend error: {e}')

with st.sidebar:
    st.header('Ingest')
    up = st.file_uploader(
        'Upload PDFs or text',
        type=['pdf','txt','md','docx'],
        accept_multiple_files=True
    )
    if st.button('Send to backend') and up:
        files = [('files', (f.name, f.getvalue())) for f in up]
        r = requests.post(f'{BACKEND}/ingest', files=files, timeout=120)
        st.success(r.json())

q = st.text_input('Ask a question about your docs')
if st.button('Search') and q:
    r = requests.post(f'{BACKEND}/query', json={'q': q}, timeout=60).json()
    st.subheader('Answer')
    st.write(r.get('answer', r))
    st.divider()
    st.subheader('Retrieved Chunks')
    for c in r.get('contexts', []):
        st.markdown(f"**{c['doc_id']} p{c['page']}** · score {c.get('score',0):.3f}")
        st.write(c['text'])