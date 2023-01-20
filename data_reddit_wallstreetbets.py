import praw
import pandas as pd

reddit = praw.Reddit(
    client_id="enter your client id here",
    client_secret="enter your client secret here",
    user_agent="enter your user agent here",
)

def get_hot_reddit_comments(number_top):
    hot_df = pd.DataFrame()
    for submission in reddit.subreddit("wallstreetbets").hot(limit=number_top):
        wallstreet_bets = {'title': submission.title}
        wallstreet_bets['score'] = submission.score
        wallstreet_bets['url'] = submission.url

        hot_df = pd.DataFrame()
        submission.comments.replace_more(limit=2)
        for comment in submission.comments.list():
            wallstreet_bets['comment'] = comment.body
            hot_df = hot_df.append(wallstreet_bets, ignore_index=True)
    
    hot_df = hot_df[hot_df['comment'] != '[deleted]']
    # hot_df = hot_df.dropna()  

    hot_df = hot_df['comment']
    return hot_df

def get_top_reddit_comments(number_top):
    top_df = pd.DataFrame()
    for submission in reddit.subreddit("wallstreetbets").top(limit=number_top):
        wallstreet_bets = {'title': submission.title}
        wallstreet_bets['score'] = submission.score
        wallstreet_bets['url'] = submission.url

        submission.comments.replace_more(limit=2)
        for comment in submission.comments.list():
            wallstreet_bets['comment'] = comment.body
            top_df = top_df.append(wallstreet_bets, ignore_index=True)

    top_df = top_df[top_df['comment'] != '[deleted]']
    # top_df = top_df.dropna()  

    top_df = top_df['comment'] 
    return top_df