from typing import List, Dict
from openai import OpenAI
from backend.settings import OPENAI_API_KEY, LLM_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

SYS = (
    "You are a careful assistant. Answer ONLY using the provided context. "
    "Cite evidence inline as [doc:{doc_id}:p{page}:{span_start}-{span_end}]. "
    "If context is insufficient, say: Not found in corpus."
)

def format_context(chunks: List[Dict]) -> str:
    lines = []
    for c in chunks:
        tag = f"[doc:{c['doc_id']}:p{c['page']}:{c['span_start']}-{c['span_end']}] "
        lines.append(tag + c['text'])
    return "\n".join(lines)

def answer(question: str, chunks: List[Dict]) -> str:
    ctx = format_context(chunks) if chunks else "NO CONTEXT"
    msg = [
        {"role": "system", "content": SYS},
        {"role": "user", "content": f"Question: {question}\n\nContext:\n{ctx}"}
    ]
    resp = client.chat.completions.create(
        model=LLM_MODEL,
        messages=msg,
        temperature=0
    )
    return resp.choices[0].message.content