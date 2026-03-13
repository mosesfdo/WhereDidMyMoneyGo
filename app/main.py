from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import statement

app = FastAPI(title="Bank Statement Analyzer API")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(statement.router, prefix="/api/statement", tags=["Statement"])

@app.get("/")
def root():
    return {"message": "Bank Statement Analyzer API is running"}
