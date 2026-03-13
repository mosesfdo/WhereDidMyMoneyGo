from pydantic import BaseModel
from typing import Optional


class Transaction(BaseModel):
    date: str
    details: str
    debit: Optional[str] = None
    credit: Optional[str] = None
    balance: Optional[str] = None


class AnalysisSummary(BaseModel):
    total_debits: float
    total_credits: float
    net_savings: float
    total_transactions: int
    debit_count: int
    credit_count: int


class Suggestion(BaseModel):
    title: str
    description: str
    priority: str  # "high", "medium", "low"


class StatementResponse(BaseModel):
    transactions: list[Transaction]
    analysis: AnalysisSummary
    suggestions: list[Suggestion]
