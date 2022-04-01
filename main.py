import tweepy
import os



CK=os.environ.get("CK")
CS=os.environ.get("CS")
AK=os.environ.get("AK")
AS=os.environ.get("AC")

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
