# AI Citation RAG
Local-first AI document search with hybrid retrieval, span-accurate citations, and an eval harness.

## Quickstart
`ash
python -m venv .venv && .\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn backend.app:app --reload
streamlit run ui/streamlit_app.py

Set-Content requirements.txt @"
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

## 🔒 Legal & Enterprise Edition

The **Legal Edition** of AI Citation RAG is designed for law firms, compliance teams, and in-house counsel.

### Additional Features
- **Advanced legal document parsing** — clause detection, exhibit linking, hierarchical structure.
- **Case citation resolution** — auto-link to public case law databases.
- **Multi-document cross-referencing** — compare contracts and flag missing clauses.
- **Compliance guardrails** — check for jurisdiction-specific requirements.
- **Bulk ingestion** — process 100+ documents at once.
- **Secure encrypted storage** — AES-256 at rest, client-controlled keys.
- **Role-based access control** — manage teams and permissions.
- **Analytics dashboard** — search patterns, risk flags, frequent clause matches.

### Availability
- Offered as **hosted SaaS** or **self-hosted license**.
- 30-day pilot program for qualifying firms.
- Pricing starts at **$49/user/month** (SaaS) or **$1,000/year** (self-hosted).

📩 **Contact**: [dustinbrown.dev@gmail.com] for a private demo or quote.