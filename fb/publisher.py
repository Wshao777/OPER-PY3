# fb/publisher.py
# OPER-PY3 Facebook 發布模組
# 遵循 OPER 原則：不儲存憑證、明確輸入、真實發布

import os
import requests
from dotenv import load_dotenv

# 從專案根目錄的 .env 檔案載入環境變數
load_dotenv()

class FacebookPublisher:
    def __init__(self):
        # 憑證從環境變數讀取，不寫死在程式碼中
        self.page_id = os.getenv("FB_PAGE_ID")
        self.access_token = os.getenv("FB_PAGE_ACCESS_TOKEN")
        
        if not self.page_id or not self.access_token:
            raise ValueError(
                "❌ 未找到 FB_PAGE_ID 或 FB_PAGE_ACCESS_TOKEN。\n"
                "請在專案根目錄建立 .env 檔案，並填入你的憑證。"
            )
        
        # Meta Graph API 端點
        self.base_url = f"https://graph.facebook.com/v19.0/{self.page_id}"

    def publish_text(self, message: str):
        """
        發布純文字貼文到 Facebook 粉絲專頁。
        
        Args:
            message: 要發布的貼文內容
        
        Returns:
            dict: API 回應，包含貼文 ID 或錯誤訊息
        """
        url = f"{self.base_url}/feed"
        payload = {
            "message": message,
            "access_token": self.access_token
        }
        
        print(f"📤 正在發布貼文到粉絲專頁 (ID: {self.page_id})...")
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ 發布成功！貼文 ID: {result.get('id')}")
            return result
        else:
            print(f"❌ 發布失敗：{response.text}")
            return response.json()

    def publish_link(self, message: str, link_url: str):
        """
        發布帶有連結的貼文（FB 會自動生成預覽卡片）。
        """
        url = f"{self.base_url}/feed"
        payload = {
            "message": message,
            "link": link_url,
            "access_token": self.access_token
        }
        
        print(f"📤 正在發布連結貼文...")
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ 發布成功！貼文 ID: {result.get('id')}")
            return result
        else:
            print(f"❌ 發布失敗：{response.text}")
            return response.json()

    def get_post_insights(self, post_id: str, metrics: list = None):
        """
        取得指定貼文的洞察數據（觸及、互動等）。
        這可以用來實現你之前想要的「流量戰情板」功能。
        """
        if metrics is None:
            metrics = ["post_impressions", "post_engaged_users", "post_reactions_by_type_total"]
        
        url = f"https://graph.facebook.com/v19.0/{post_id}/insights"
        params = {
            "metric": ",".join(metrics),
            "access_token": self.access_token
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ 取得洞察數據失敗：{response.text}")
            return None
