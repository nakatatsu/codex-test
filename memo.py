class Memo:
    """Simple memo class to store a text message."""

    def __init__(self, text: str):
        self.text = text

    def __repr__(self) -> str:
        return f"Memo({self.text!r})"

    def __str__(self) -> str:
        return self.text
