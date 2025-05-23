import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import memo


def setup_store(tmp_path, monkeypatch):
    data_dir = tmp_path / "data"
    monkeypatch.setattr(memo, "DATA_DIR", str(data_dir))
    store = memo.MemoStore()
    return store, data_dir


def test_add_and_get_memo(tmp_path, monkeypatch):
    store, data_dir = setup_store(tmp_path, monkeypatch)
    memo_id = store.add_memo("hello")
    assert (data_dir / f"{memo_id}.txt").read_text() == "hello"
    memo_obj = store.get_memo(memo_id)
    assert memo_obj is not None
    assert str(memo_obj) == "hello"
    assert store.get_memo("nonexistent") is None


def test_update_memo(tmp_path, monkeypatch):
    store, _ = setup_store(tmp_path, monkeypatch)
    memo_id = store.add_memo("first")
    assert store.update_memo(memo_id, "second") is True
    assert store.get_memo(memo_id).text == "second"
    assert store.update_memo("missing", "x") is False


def test_delete_memo(tmp_path, monkeypatch):
    store, data_dir = setup_store(tmp_path, monkeypatch)
    memo_id = store.add_memo("bye")
    assert store.delete_memo(memo_id) is True
    assert not (data_dir / f"{memo_id}.txt").exists()
    assert store.delete_memo(memo_id) is False


def test_list_memos(tmp_path, monkeypatch):
    store, _ = setup_store(tmp_path, monkeypatch)
    ids = [store.add_memo(f"text{i}") for i in range(3)]
    listed = dict(store.list_memos())
    assert set(listed.keys()) == set(ids)
    for i, memo_id in enumerate(ids):
        assert listed[memo_id].text == f"text{i}"
