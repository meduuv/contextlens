"""Context size statistics."""


def stats(text: str) -> dict[str, int]:
    """Return character, word, line and paragraph counts."""
    return {
        "characters": len(text),
        "words": len(text.split()),
        "lines": 0 if not text else len(text.splitlines()),
        "paragraphs": 0 if not text.strip() else len([p for p in text.split("\n\n") if p.strip()]),
    }
