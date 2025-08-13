import os, shutil, uuid, json
from pathlib import Path
from backend.settings import RAW_DIR, PROC_DIR
from backend.utils.pdf import pdf_to_pages
from backend.ingest.chunkers import split_text, to_records
from backend.index.faiss_store import FaissStore

def ingest_file(src_path: str) -> str:
    os.makedirs(RAW_DIR, exist_ok=True); os.makedirs(PROC_DIR, exist_ok=True)
    doc_id = str(uuid.uuid4())[:8]; ext = Path(src_path).suffix.lower()
    dst = f'{RAW_DIR}/{doc_id}{ext}'; shutil.copy2(src_path, dst)
    records=[]
    if ext=='.pdf':
        for page, text in pdf_to_pages(dst):
            chunks = split_text(text); records += to_records(doc_id, page, chunks)
    else:
        text = Path(src_path).read_text(encoding='utf-8', errors='ignore')
        chunks = split_text(text); records += to_records(doc_id, 1, chunks)
    with open(f'{PROC_DIR}/{doc_id}.json','w',encoding='utf-8') as f: json.dump(records,f)
    return doc_id

def rebuild_index():
    store = FaissStore(); allrecs=[]
    for p in Path(PROC_DIR).glob('*.json'):
        allrecs += json.loads(Path(p).read_text(encoding='utf-8'))
    store.add(allrecs); store.build()
