import requests

class LineClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://api.line.me"
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    def get_profile(self):
        # 自分のプロフィールを取得
        profile_url = f"{self.base_url}/v2/profile"
        response = requests.get(profile_url, headers=self.headers)
        return response.json()

    def send_message(self, to, text):
        # テキストメッセージを送信
        message_url = f"{self.base_url}/v2/bot/message/push"
        data = {
            "to": to,
            "messages": [{
                "type": "text",
                "text": text
            }]
        }
        response = requests.post(message_url, headers=self.headers, json=data)
        return response.json()

    def get_group_members(self, group_id):
        # グループメンバーを取得
        group_members_url = f"{self.base_url}/v2/bot/group/{group_id}/members"
        response = requests.get(group_members_url, headers=self.headers)
        return response.json()