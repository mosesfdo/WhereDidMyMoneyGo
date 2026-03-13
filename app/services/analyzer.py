import re


def parse_amount(amount_str: str) -> float:
    """Convert 'INR 1,200.00' to 1200.0"""
    if not amount_str:
        return 0.0
    cleaned = re.sub(r"[^\d.]", "", amount_str)
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def analyze_transactions(transactions: list) -> dict:
    """Analyze transactions and return summary statistics."""
    total_debits = 0.0
    total_credits = 0.0
    debit_transactions = []
    credit_transactions = []

    for txn in transactions:
        if txn.get("debit"):
            amount = parse_amount(txn["debit"])
            total_debits += amount
            debit_transactions.append({**txn, "amount": amount})
        if txn.get("credit"):
            amount = parse_amount(txn["credit"])
            total_credits += amount
            credit_transactions.append({**txn, "amount": amount})

    # Top 5 highest expenses
    top_expenses = sorted(debit_transactions, key=lambda x: x["amount"], reverse=True)[:5]

    return {
        "total_debits": round(total_debits, 2),
        "total_credits": round(total_credits, 2),
        "net_savings": round(total_credits - total_debits, 2),
        "total_transactions": len(transactions),
        "debit_count": len(debit_transactions),
        "credit_count": len(credit_transactions),
        "top_expenses": top_expenses,
    }
