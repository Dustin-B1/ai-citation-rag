import re
def split_text(text: str, max_tokens=900, overlap=150):
    sents = re.split(r'(?<=[.!?])\s+', text)
    chunks, cur, count = [], [], 0
    for s in sents:
        t = len(s.split())
        if count + t > max_tokens and cur:
            chunks.append(' '.join(cur))
            back = ' '.join(' '.join(cur).split()[-overlap:])
            cur = [back, s]; count = len(back.split()) + t
        else:
            cur.append(s); count += t
    if cur: chunks.append(' '.join(cur))
    return chunks
def to_records(doc_id, page, chunks):
    recs=[]; start=0
    for c in chunks:
        end = start + len(c)
        recs.append({'doc_id':doc_id,'page':page,'text':c,'span_start':start,'span_end':end})
        start=end
    return recs
