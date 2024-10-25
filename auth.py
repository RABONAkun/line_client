import requests
import qrcode
import json

class LineAuth:
    def __init__(self):
        self.base_url = "https://legy-jp.line.naver.jp"  # LINEの認証エンドポイント
        self.session = requests.Session()
        self.access_token = None

    def login_with_qr_code(self):
        # QRコードを使った認証処理
        qr_login_url = f"{self.base_url}/acct/lgn/sso/qr"
        response = self.session.post(qr_login_url)
        qr_data = response.json().get('qr_code')
        img = qrcode.make(qr_data)
        img.show()
        print("QRコードをスキャンしてください")

    def check_login_status(self):
        # QRコードスキャン後に認証トークンを取得
        check_url = f"{self.base_url}/acct/lgn/sso/status"
        response = self.session.get(check_url)
        if response.status_code == 200 and 'access_token' in response.json():
            self.access_token = response.json()['access_token']
            print("ログイン成功")
        else:
            print("ログイン失敗")