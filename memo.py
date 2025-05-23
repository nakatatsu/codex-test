import os
import uuid
from dataclasses import dataclass

# Directory where individual memo files are stored
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

@dataclass
class Memo:
    """Simple memo class to store a text message."""

    text: str

    def __str__(self) -> str:
        return self.text


class MemoStore:
    """Store memos as individual text files identified by UUID."""

    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)

    def _memo_path(self, memo_id: str) -> str:
        return os.path.join(DATA_DIR, f"{memo_id}.txt")

    def add_memo(self, content: str) -> str:
        """Create a new memo with a UUID and save it."""
        memo_id = str(uuid.uuid4())
        with open(self._memo_path(memo_id), "w", encoding="utf-8") as f:
            f.write(content)
        return memo_id

    def get_memo(self, memo_id: str):
        """Retrieve a memo by UUID."""
        path = self._memo_path(memo_id)
        if not os.path.exists(path):
            return None
        with open(path, "r", encoding="utf-8") as f:
            return Memo(f.read())

    def update_memo(self, memo_id: str, content: str) -> bool:
        """Update an existing memo. Returns True if it exists."""
        path = self._memo_path(memo_id)
        if not os.path.exists(path):
            return False
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True

    def delete_memo(self, memo_id: str) -> bool:
        """Delete a memo file by UUID."""
        path = self._memo_path(memo_id)
        if not os.path.exists(path):
            return False
        os.remove(path)
        return True

    def list_memos(self):
        """List all memos as tuples of (uuid, Memo)."""
        memos = []
        for filename in os.listdir(DATA_DIR):
            if filename.endswith(".txt"):
                memo_id = filename[:-4]
                memo = self.get_memo(memo_id)
                if memo is not None:
                    memos.append((memo_id, memo))
        return memos
