# Bank Statement Analyzer - Backend

A FastAPI backend that parses bank statements and returns AI-powered financial suggestions.

## Setup

1. **Clone the repo and navigate to backend/**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**
   - Open the `.env` file
   - Replace `your_api_key_here` with your Anthropic API key

5. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Test it**
   - Open your browser at: http://localhost:8000
   - API docs available at: http://localhost:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/statement/upload` | Upload a bank statement file |

## Supported File Types
- `.xlsx` — Excel
- `.csv` — CSV
- `.pdf` — PDF

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Environment variables
│   ├── models.py            # Pydantic models
│   ├── utils.py             # Helper functions
│   ├── routes/
│   │   └── statement.py     # Upload route
│   └── services/
│       ├── parser.py        # File parsing logic
│       ├── analyzer.py      # Transaction analysis
│       └── ai_service.py    # Claude AI suggestions
├── uploads/                 # Temporary file storage
├── tests/
├── .env                     # API keys (do NOT commit)
├── .gitignore
├── requirements.txt
└── README.md
```
