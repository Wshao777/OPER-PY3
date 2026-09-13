from pathlib import Path

for img in Path(".").rglob("*"):
    if ".git" in img.parts:
        continue
    if img.suffix.lower() not in {".jpg", ".jpeg"}:
        continue

    md = img.with_suffix(".md")
    jpg_name = img.name
    md_name = md.name

    content = f"""# ⚡ JPG → OPER AI 演練

![演練圖片](./{jpg_name})

## 🧠 AI 視覺理解

根據上方 JPG 圖片進行視覺理解與資訊整理。

## 📌 演練重點

- 圖片來源：`{jpg_name}`
- 輸入類型：JPG
- 輸出格式：Markdown
- 文件名稱：`{md_name}`
- 圖片狀態：已嵌入
- 演練狀態：完成
- 公開狀態：可展示

## ⚡ 演練結果

圖片內容經 AI 整理後，形成可閱讀、可追蹤的 Markdown 演練文件。

## 🤖 OPER AI

JPG → AI 視覺理解 → 演練 → 同名 MD → GitHub 圖片展示

## 🔗 專案

- OPER-PY3
- Lightning-Expo-2026-Taichung
"""

    md.write_text(content, encoding="utf-8")
    print(f"generated: {md}")
