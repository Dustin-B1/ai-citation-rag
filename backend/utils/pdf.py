import fitz  # PyMuPDF
def pdf_to_pages(path: str):
    doc = fitz.open(path)
    for i in range(len(doc)):
        yield i+1, doc[i].get_text('text')
