import json
import os
from dataclasses import dataclass

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
MEMO_FILE = os.path.join(DATA_DIR, "memos.json")

@dataclass
class Memo:
    """Simple memo class to store a text message."""

    text: str

    def __str__(self) -> str:
        return self.text


class MemoStore:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.memos = {}
        if os.path.exists(MEMO_FILE):
            with open(MEMO_FILE, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, dict):
                        self.memos = {k: Memo(v) for k, v in data.items()}
                except json.JSONDecodeError:
                    self.memos = {}

    def _save(self):
        with open(MEMO_FILE, 'w', encoding='utf-8') as f:
            json.dump({k: memo.text for k, memo in self.memos.items()}, f, ensure_ascii=False, indent=2)

    def add_memo(self, content: str) -> str:
        if self.memos:
            new_id = str(max(int(k) for k in self.memos.keys()) + 1)
        else:
            new_id = "1"
        self.memos[new_id] = Memo(content)
        self._save()
        return new_id

    def get_memo(self, memo_id: str):
        return self.memos.get(str(memo_id))

    def list_memos(self):
        return [(memo_id, self.memos[memo_id]) for memo_id in sorted(self.memos.keys(), key=lambda x: int(x))]

