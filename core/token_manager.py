"""Token budgeting for swarm reports ("Token Fracture").

Estimates tokens at ~4 characters each and truncates oversized reports to a
budget so downstream LLM-backed steps stay within context limits. Deliberately
simple: no claim of semantic compression is made.
"""


class TokenManager:
    def __init__(self, chars_per_token: int = 4):
        if chars_per_token <= 0:
            raise ValueError("chars_per_token must be a positive integer")
        self.chars_per_token = chars_per_token

    def estimate_tokens(self, text: str) -> int:
        return max(1, len(text) // self.chars_per_token)

    def fracture(self, text: str, max_tokens: int = 4000) -> str:
        """Cut text down to a token budget, keeping the head of the report.

        The truncation notice is reserved inside the budget: the returned text
        never exceeds max_tokens estimated tokens.
        """
        budget_chars = max_tokens * self.chars_per_token
        if len(text) <= budget_chars:
            return text
        notice = f"\n\n[... truncated by TokenManager: {self.estimate_tokens(text)} estimated tokens > {max_tokens} budget]"
        cut = text[: max(0, budget_chars - len(notice))]
        return cut + notice
