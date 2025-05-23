This repository demonstrates simple Python classes.

`memo.py` defines a `Memo` dataclass and a `MemoStore` that stores each memo in
separate files under the `./data` directory. Each memo is identified by a UUID
so updates and deletions are performed using that ID.

`main.py` provides a command line interface to manage these memos. Example
usage:

```
$ python main.py add "Buy milk"
<uuid>
$ python main.py list
<uuid>: Buy milk
```
