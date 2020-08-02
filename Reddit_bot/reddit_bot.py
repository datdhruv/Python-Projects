import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("pythonforengineers")

for submission in subreddit.new(limit=5):
    print("Title: ", submission.title)
    #print("Text: ", submission.text)
    print("Score: ", submission.score)
    print("-----------------------------\n")
