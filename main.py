import tweepy


CK = "sHdXaO0oNTDh7KK3OQCzhw75N"
CS = "hceggx0eFZ7xWV4TfPwfCo5rFBOIk9kv3dH0UUzGLhNIBGSlY9"

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(auth.access_token, auth.access_token_secret)

api = tweepy.API(auth)

# 1ツイートずつループ
for status in api.search(q='#またたび質問箱英語', count=50):
    tweet_id = status.id
    # 例外処理をする
    try:
        # リツイート実行
        api.retweet(tweet_id)
    except:
        print('error')
