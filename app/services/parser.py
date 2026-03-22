import pandas as pd
import pdfplumber
import re


def parse_statement(file_path: str, ext: str) -> list:
    """Parse bank statement file and return list of transactions."""
    if ext == ".xlsx":
        return parse_excel(file_path)
    elif ext == ".csv":
        return parse_csv(file_path)
    elif ext == ".pdf":
        return parse_pdf(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")


def parse_excel(file_path: str) -> list:
    df = pd.read_excel(file_path, header=None)
    return extract_transactions(df)


def parse_csv(file_path: str) -> list:
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def parse_pdf(file_path: str) -> list:
    transactions = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table[1:]:  # Skip header row
                    transactions.append(row)
    return transactions


def extract_transactions(df: pd.DataFrame) -> list:
    """Extract transactions from a DataFrame with unknown structure."""
    transactions = []
    for i, row in df.iterrows():
        date_val = str(row.iloc[1]).strip()
        if re.match(r"\d{2} \w+ \d{4}", date_val):
            debit = str(row.iloc[10]).strip()
            credit = str(row.iloc[13]).strip()
            transactions.append({
                "date": date_val,
                "details": str(row.iloc[2]).strip(),
                "debit": None if debit in ["-", "nan", "NaN"] else debit,
                "credit": None if credit in ["-", "nan", "NaN"] else credit,
                "balance": str(row.iloc[15]).strip()
            })
    return transactions
