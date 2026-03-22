import re


def clean_amount(amount_str: str) -> float:
    """Convert currency string like 'INR 1,200.00' to float 1200.0"""
    if not amount_str:
        return 0.0
    cleaned = re.sub(r"[^\d.]", "", str(amount_str))
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def is_date(value: str) -> bool:
    """Check if a string matches date format like '21 Feb 2026'"""
    return bool(re.match(r"\d{2} \w+ \d{4}", str(value).strip()))


def sanitize_filename(filename: str) -> str:
    """Remove unsafe characters from filename"""
    return re.sub(r"[^\w.\-]", "_", filename)
