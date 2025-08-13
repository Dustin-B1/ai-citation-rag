from dotenv import load_dotenv; load_dotenv()
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os, shutil
from backend.ingest.pipeline import ingest_file, rebuild_index
from backend.rag.retriever import init_store, retrieve
from backend.rag.answerer import answer

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['*'], allow_methods=['*'])

@app.on_event('startup')
def _startup():
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('data/index', exist_ok=True)
    init_store()

@app.get('/health')
def health(): return {'ok': True}

@app.post('/ingest')
async def ingest(files: List[UploadFile] = File(...)):
    ids=[]
    for f in files:
        tmp = f'tmp_{f.filename}'
        with open(tmp,'wb') as out: shutil.copyfileobj(f.file, out)
        ids.append(ingest_file(tmp))
        os.remove(tmp)
    rebuild_index()
    return {'doc_ids': ids}

@app.post('/query')
async def query(q: str = Form(...)):
    chunks = retrieve(q, k=6)
    ans = answer(q, chunks)
    return {'answer': ans, 'contexts': chunks}
