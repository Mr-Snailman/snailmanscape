import json
import os
import praw
import sys

class RedditCommander:
    def __init__(self, reddit):
        self.reddit = reddit

    def post(self, subredditStr='rarepuppers', numPosts=50):
        posts = self.reddit.subreddit(subredditStr).hot(limit=numPosts)
        for submission in posts:
            print(submission.url)

class ConfigService:
    def __init__(self):
        f = open(os.path.abspath(os.path.join(os.path.dirname(__file__), "config", "config.json")), "r")
        self.config = json.loads(f.read())

def main():
    config = ConfigService().config
    reddit = praw.Reddit(
        client_id=config["client_id"],
        client_secret=config["client_secret"],
        password=config["password"],
        user_agent=config["user_agent"], 
        username=config["username"]
        )

    scrapeBot = RedditCommander(reddit)
    scrapeBot.post()

main()
