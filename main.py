# main.py (OPER Core 主入口)
from fb.publisher import FacebookPublisher

def main():
    print("="*60)
    print("OPER Core | Facebook 發布模組")
    print("="*60)
    
    # 初始化發布器
    try:
        publisher = FacebookPublisher()
    except ValueError as e:
        print(e)
        print("\n💡 請在專案根目錄建立 .env 檔案，並填入 FB_PAGE_ID 與 FB_PAGE_ACCESS_TOKEN")
        return
    
    # 選擇操作
    while True:
        print("\n[1] 發布純文字貼文")
        print("[2] 發布連結貼文")
        print("[3] 查詢貼文洞察數據")
        print("[4] 退出")
        choice = input("請選擇操作 (1-4): ")
        
        if choice == '1':
            message = input("請輸入貼文內容：\n")
            publisher.publish_text(message)
            
        elif choice == '2':
            message = input("請輸入貼文內容：\n")
            link = input("請輸入連結網址：\n")
            publisher.publish_link(message, link)
            
        elif choice == '3':
            post_id = input("請輸入貼文 ID：\n")
            insights = publisher.get_post_insights(post_id)
            if insights:
                print("\n📊 洞察數據：")
                for metric in insights.get("data", []):
                    print(f"  {metric['name']}: {metric['values']}")
                    
        elif choice == '4':
            print("👋 再見！")
            break
        else:
            print("無效選擇，請重試。")

if __name__ == "__main__":
    main()
    
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
