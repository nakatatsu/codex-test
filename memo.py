import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
MEMO_FILE = os.path.join(DATA_DIR, "memos.json")

class MemoStore:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        if os.path.exists(MEMO_FILE):
            with open(MEMO_FILE, 'r', encoding='utf-8') as f:
                try:
                    self.memos = json.load(f)
                except json.JSONDecodeError:
                    self.memos = {}
        else:
            self.memos = {}

    def _save(self):
        with open(MEMO_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.memos, f, ensure_ascii=False, indent=2)

    def add_memo(self, content: str) -> str:
        if self.memos:
            new_id = str(max(int(k) for k in self.memos.keys()) + 1)
        else:
            new_id = "1"
        self.memos[new_id] = content
        self._save()
        return new_id

    def get_memo(self, memo_id: str) -> str:
        return self.memos.get(str(memo_id))

    def list_memos(self):
        return [(memo_id, self.memos[memo_id]) for memo_id in sorted(self.memos.keys(), key=lambda x: int(x))]
