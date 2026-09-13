from pathlib import Path

for img in Path(".").rglob("*"):
    if ".git" in img.parts or "private" in img.parts:
        continue
    if img.suffix.lower() not in {".jpg", ".jpeg"}:
        continue

    md = img.with_suffix(".md")
    jpg_name = img.name
    md_name = md.name

    content = f"""# ⚡ JPG → OPER AI 演練

![演練圖片](./{jpg_name})

## 📌 演練聲明

本文件為 OPER AI 自動生成之視覺演練記錄，僅包含圖片與演練結果。  
架構、程式碼、AI 對話與私有邏輯均不公開。

## 🔗 專案

- OPER-PY3
- Lightning-Expo-2026-Taichung

---
> 公開演練文件 · 僅展示圖片與聲明
"""

    md.write_text(content, encoding="utf-8")
    print(f"generated: {md}")
