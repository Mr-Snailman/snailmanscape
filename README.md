# snailmanscape

Requirements:

* python 3.x
* pip3 (via [Pipfile](https://github.com/pypa/pipfile))
* [pipenv](https://docs.pipenv.org/)

To Run:

```bash
pipenv install
pipenv shell
python3 reddit-scrape.py
```

In the config/ directory, create a file named 'config.json' in the following format:
```json
{
  "client_id":"Your Reddit Client ID",
  "client_secret":"Your Reddit Client Secret",
  "password":"Your Reddit API Password",
  "user_agent":"Python3 snailmanscape script",
  "username":"Your Reddit API Username",
  "subreddits":["subreddit1", "subreddit2"]	
}
```
