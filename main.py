from auth import LineAuth
from client import LineClient
from polling import LinePolling

def main():
    # 認証処理
    auth = LineAuth()
    auth.login_with_qr_code()
    auth.check_login_status()

    if auth.access_token:
        # クライアントインスタンスの生成
        client = LineClient(auth.access_token)

        # プロフィール取得
        profile = client.get_profile()
        print(f"ログインユーザー: {profile['displayName']}")

        # メッセージ送信
        to = input("送信先ユーザーID: ")
        message = input("送信するメッセージ: ")
        result = client.send_message(to, message)
        print("メッセージ送信結果: ", result)

        # ポーリング開始（メッセージやイベントを取得）
        polling = LinePolling(client)
        polling.start_polling()
    else:
        print("ログインに失敗しました。")

if __name__ == "__main__":
    main()