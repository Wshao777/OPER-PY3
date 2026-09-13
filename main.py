import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def banner():
    print("=" * 60)
    print("OPER-PY3")
    print("AI DEVELOPMENT ENTRY")
    print("=" * 60)


def create_structure():

    folders = [
        "core",
        "ai",
        "bot",
        "fb",
        "data",
        "logs"
    ]

    for name in folders:
        path = ROOT / name
        path.mkdir(
            parents=True,
            exist_ok=True
        )

    memory = ROOT / "data" / "memory.json"

    if not memory.exists():
        memory.write_text(
            '{"entries":[]}',
            encoding="utf-8"
        )

    print("OPER structure ready.")


def start_ai():

    print()
    print("[AI MODE]")
    print()
    print("Enter text.")
    print("Type EXIT to return.")
    print()

    while True:

        text = input("OPER AI > ").strip()

        if text.upper() == "EXIT":
            break

        if not text:
            continue

        print()
        print("AI INPUT:")
        print(text)
        print()
        print("AI engine ready.")
        print()


def main():

    banner()

    create_structure()

    while True:

        print()
        print("[1] AI")
        print("[2] Create project structure")
        print("[3] Exit")

        choice = input("> ").strip()

        if choice == "1":
            start_ai()

        elif choice == "2":
            create_structure()

        elif choice == "3":
            print("OPER stopped.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
