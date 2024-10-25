import time
import requests

class LinePolling:
    def __init__(self, client):
        self.client = client
        self.poll_url = f"{self.client.base_url}/v2/bot/poll"

    def fetch_events(self):
        # メッセージやイベントをポーリングで取得
        response = requests.get(self.poll_url, headers=self.client.headers)
        if response.status_code == 200:
            events = response.json().get('events', [])
            for event in events:
                self.handle_event(event)
        else:
            print("ポーリング失敗")

    def handle_event(self, event):
        # メッセージイベントなどを処理
        if event['type'] == 'message':
            message = event['message']
            print(f"新着メッセージ: {message['text']}")
        else:
            print(f"新着イベント: {event['type']}")

    def start_polling(self):
        # ポーリング開始
        while True:
            self.fetch_events()
            time.sleep(2)  # 一定時間待機してから次のポーリングを行う