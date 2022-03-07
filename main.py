import tweepy


CK = "sHdXaO0oNTDh7KK3OQCzhw75N"
CS = "hceggx0eFZ7xWV4TfPwfCo5rFBOIk9kv3dH0UUzGLhNIBGSlY9"

AK="1500064603836870659-y3vFNvAt0nlQO2GKfvdTmTfElGKyyE"
AS="i0WwHsm7CRbWXJIeQ3uAdnbJ4BthSjoKToFGSFERC6Rvv"


# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AK, AS)

api = tweepy.API(auth)

# 1ツイートずつループ。
for status in api.search(q='#またたび万葉集', count=50):
    tweet_id = status.id
    # 例外処理をする
    try:
        # リツイート実行
        api.retweet(tweet_id)
    except:
        print('error')
