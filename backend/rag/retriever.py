from backend.index.faiss_store import FaissStore
store = FaissStore()
def init_store(): store.load()
def retrieve(q: str, k=6): return store.search(q, k=k)
