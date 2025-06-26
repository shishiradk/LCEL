# 🌐 LCEL Language Translator

A minimal LCEL-based app to perform language translation using large language models (LLMs). Built by [@shishiradk](https://github.com/shishiradk) with LangChain Expression Language (LCEL) and deployed via LangServe.

---

## ✨ Features

- Translate text between languages using simple LCEL chains
- Fast API endpoint served with LangServe
- Ready to run locally or deploy to cloud

---

## 🧱 File Structure

```
├── client.py              # Test client to interact with the server
├── serve.py               # Main LangServe app entry point
├── simplellmLCEL.ipynb    # Notebook for interactive LCEL prototyping
├── requirements.txt       # Python dependencies
├── README.md              # Project overview
├── LICENSE                # MIT License
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/shishiradk/LCEL.git
cd LCEL
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file and add your OpenAI key:

```env
OPENAI_API_KEY=your_key_here
```

### 4. Run the app

```bash
python serve.py
```

The server will start at: `http://localhost:8000/`

---

## 🧪 Test the Translation API

Run the client:

```bash
python client.py
```

Or send a direct request (e.g., via `curl` or Postman):

```json
POST /invoke

{
  "input": {
    "language": "french",
    "text": "hello my mame is shishir"
  },
  "config": {},
  "kwargs": {}
}
```

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
