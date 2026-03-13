import anthropic
import json
from app.config import settings


def get_ai_suggestions(analysis: dict) -> list:
    """Send analysis to Claude and get financial suggestions."""
    client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    prompt = f"""
You are a personal finance advisor. Based on the following bank statement analysis, 
provide 5 specific, actionable suggestions to help the user be more financially efficient.

Analysis:
{json.dumps(analysis, indent=2)}

Return your response as a JSON array of suggestions. Each suggestion should have:
- "title": short title
- "description": detailed explanation
- "priority": "high", "medium", or "low"

Return ONLY the JSON array, no extra text.
"""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()
    return json.loads(raw)
