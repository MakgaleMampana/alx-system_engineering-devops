#!/usr/bin/python3
"""Module that queries the Reddit API and prints the first 10 hot posts listed
for the subreddit."""
import requests


def top_ten(subreddit):
    """Function that sends a request to the Reddit API and takes a subreddit
    as parameter, then displays the title of the top ten hot posts.

    subreddit: the subredit to query"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers={'user-agent': 'request'},
                            allow_redirects=False)
    if response.status_code != requests.codes.ok:
        print(None)
        return
    rdict = response.json()
    posts = rdict.get('data').get('children')
    for post in posts:
        print(post.get('data').get('title'))
