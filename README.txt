# Readme

This repository demonstrates simple Python classes.

This project was created with ChatGPT Codex.

`memo.py` defines a `Memo` dataclass and a `MemoStore` that stores each memo in
separate files under the `./data` directory. Each memo is identified by a UUID
so updates and deletions are performed using that ID.

`main.py` provides a command line interface to manage these memos. Available
commands are:

- `add` - create a new memo
- `list` - list all existing memos
- `get` - retrieve a memo by its UUID
- `update` - change the text of a memo
- `delete` - remove a memo

Example usage:

```
$ python main.py add "Buy milk"
<uuid>
$ python main.py list
<uuid>: Buy milk
$ python main.py get <uuid>
Buy milk
$ python main.py update <uuid> "Buy eggs"
Updated
$ python main.py delete <uuid>
Deleted
```
