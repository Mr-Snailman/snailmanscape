#!/usr/bin/env python3

import json
import os
import praw
import shutil
import sys
import urllib.request

localStore = "/srv/reddit/"

class RedditCommander:
    def __init__(self, config, reddit):
        self.config = config
        self.reddit = reddit

    def scrapePosts(self, numPosts=25):
        for subredditStr in self.config["subreddits"]:
            if not os.path.exists(localStore + subredditStr):
                os.makedirs(localStore + subredditStr)

            posts = self.reddit.subreddit(subredditStr).hot(limit=numPosts)
            for submission in posts:
                if "comments" not in submission.url:
                    filename = localStore + subredditStr + "/" + submission.url.split('/')[-1]
                    if not os.path.exists(filename):
                        with urllib.request.urlopen(submission.url) as response, open(filename, 'wb') as out_file:
                            shutil.copyfileobj(response, out_file)
                    else:
                        print("Already have that one... " + filename)

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

    scrapeBot = RedditCommander(config, reddit)
    scrapeBot.scrapePosts()

main()
