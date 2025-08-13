import os, json, numpy as np, faiss
from typing import List, Dict
from openai import OpenAI
from backend.settings import OPENAI_API_KEY, EMBED_MODEL, INDEX_DIR
client = OpenAI(api_key=OPENAI_API_KEY)

class FaissStore:
    def __init__(self, name='faiss'):
        self.meta_path=f'{INDEX_DIR}/{name}.meta.json'
        self.index_path=f'{INDEX_DIR}/{name}.index'
        os.makedirs(INDEX_DIR, exist_ok=True)
        self.texts=[]; self.metas=[]; self.index=None
    def _embed(self, texts: List[str]) -> np.ndarray:
        resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
        return np.array([d.embedding for d in resp.data], dtype='float32')
    def add(self, recs: List[Dict]):
        self.texts += [r['text'] for r in recs]; self.metas += recs
    def build(self):
        vecs = self._embed(self.texts) if self.texts else np.zeros((0,1536),'float32')
        if vecs.size==0: 
            self.index = faiss.IndexFlatIP(1536); faiss.write_index(self.index, self.index_path)
            with open(self.meta_path,'w',encoding='utf-8') as f: json.dump(self.metas,f); return
        d = vecs.shape[1]; self.index = faiss.IndexFlatIP(d)
        faiss.normalize_L2(vecs); self.index.add(vecs)
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path,'w',encoding='utf-8') as f: json.dump(self.metas,f)
    def load(self):
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.meta_path,'r',encoding='utf-8') as f: self.metas = json.load(f)
            self.texts = [m['text'] for m in self.metas]
    def search(self, query: str, k=5):
        if not self.index: self.load()
        qv = self._embed([query]); faiss.normalize_L2(qv)
        D,I = self.index.search(qv, k)
        out=[]
        for idx, score in zip(I[0], D[0]):
            if idx==-1: continue
            rec = dict(self.metas[idx]); rec['score']=float(score); out.append(rec)
        return out
