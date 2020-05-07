#!/usr/bin/python3
""" Request Reddit API """
import requests


def recurse(subreddit, hot_list=[], url=
            'https://www.reddit.com/r/{}/hot.json'):
    """  Recurse it!  """
    url = url.format(subreddit)
    tok = {'user-agent': 'X-Modhash'}
    req = requests.get(url, headers=tok)
    if req.history or req.status_code == 404:
        return None
    req = req.json()
    after = req.get('data').get('after')
    if after:
        req = req.get('data').get('children')
        for title in req:
            title = title.get('data').get('title')
            hot_list.append(title)
        return recurse(subreddit, hot_list,
                       'https://www.reddit.com/r/{}/hot.json?after=' + after)
    else:
        return hot_list
