"""Command-line interface to manage memos using :mod:`memo`."""

import argparse

from memo import MemoStore


def main() -> None:
    """Entry point for memo operations."""
    parser = argparse.ArgumentParser(description="Simple memo manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Create a new memo")
    add_parser.add_argument("text", help="Text content for the memo")

    get_parser = subparsers.add_parser("get", help="Retrieve a memo by ID")
    get_parser.add_argument("id", help="Memo UUID")

    update_parser = subparsers.add_parser("update", help="Update an existing memo")
    update_parser.add_argument("id", help="Memo UUID")
    update_parser.add_argument("text", help="New text content")

    delete_parser = subparsers.add_parser("delete", help="Delete a memo")
    delete_parser.add_argument("id", help="Memo UUID")

    subparsers.add_parser("list", help="List all memos")

    args = parser.parse_args()
    store = MemoStore()

    if args.command == "add":
        memo_id = store.add_memo(args.text)
        print(memo_id)
    elif args.command == "get":
        memo = store.get_memo(args.id)
        if memo is None:
            print("Memo not found")
        else:
            print(memo)
    elif args.command == "update":
        success = store.update_memo(args.id, args.text)
        print("Updated" if success else "Memo not found")
    elif args.command == "delete":
        success = store.delete_memo(args.id)
        print("Deleted" if success else "Memo not found")
    elif args.command == "list":
        for memo_id, memo in store.list_memos():
            print(f"{memo_id}: {memo}")


if __name__ == "__main__":
    main()

