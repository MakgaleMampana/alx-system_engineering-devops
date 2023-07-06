#!/usr/bin/python3
"""Module that queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Function that sends a request to the Reddit API and takes a subreddit
    as parameter, then recursively returns a list of the posts' title.

    subreddit: the subredit to query
    hot_list: the list of titles
    after: the after tag for the next page"""
    # Check if already at last page
    if after is None:
        return []

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    response = requests.get(url, headers={'user-agent': 'request'},
                            allow_redirects=False)
    if response.status_code != requests.codes.ok:
        return None
    rdict = response.json()
    posts = rdict.get('data').get('children')
    for post in posts:
        post_title = post.get('data').get('title')
        hot_list.append(post_title)
    return hot_list + recurse(subreddit, [], rdict.get('data').get('after'))
