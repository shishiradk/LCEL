# LCEL-Teacher

An intelligent assistant that helps users learn and explore the LangChain Expression Language (LCEL) via multiple architectures like RAG, context-stuffing, and chain recovery.

## 🚀 Overview

**LCEL-Teacher** is a LangChain-powered application designed to teach and support users working with LCEL. It showcases different architectures:

- **Context Stuffing**: Injects LCEL documentation into the prompt.
- **RAG**: Retrieves relevant chunks from LangChain documentation via vector search.
- **Multi-QA RAG**: Uses multiple QA pairs for richer context.
- **Recovery via LangGraph**: Automatically retries execution for failed chains.

All chains are deployed via LangServe and exposed as endpoints.

---

## 🧠 Architectures

Each chain is under `/app`:

- `context_stuffing.py`
- `rag.py`
- `multi_qa_rag.py`
- `recovery_graph.py`

Embeddings are powered by Voyage AI, and the vector store is Weaviate.

---

## 🔧 Installation

### Prerequisites

- Python 3.10+
- Poetry

### Environment Variables

```env
WEAVIATE_URL=your_weaviate_url
WEAVIATE_API_KEY=your_api_key
VOYAGE_API_KEY=your_voyage_api_key
VOYAGE_AI_MODEL=your_model_name
```

### Install Dependencies

```bash
poetry install
```

### Run Locally

```bash
poetry run langchain serve
```

---

## 🧪 Evaluation

Evaluation notebooks are provided under `/eval`. You can:

- Run chain performance tests
- Compare output quality

Use `eval/eval_lcel_teacher.ipynb` to get started.

---

## 📁 Project Structure

```
/app                # Chain implementations
/eval               # Evaluation notebooks
/ntbk               # Prototyping and experiments
Dockerfile          # Container configuration
pyproject.toml      # Dependencies and project metadata
README.md           # Project overview
```

---

## 📬 API Usage

After serving locally, send a POST request to:

```
http://localhost:8000/lcel-teacher
```

With a JSON body like:

```json
{
  "question": "How do I use map_chain in LCEL?"
}
```

---

## 🙌 Credits

Built using LangServe, LangGraph, and LangChain.

---

## 📜 License

MIT License. See `LICENSE` file for details.
# LCEL
