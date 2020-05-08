#!/usr/bin/python3
""" Request Reddit API """
import requests


def count_words(subreddit, word_list, after=''):
    """  Recurse it!  """
    url = 'https://www.reddit.com/r/{}/\
hot.json?after={}'.format(subreddit, after)
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
        print('{}: '.format(word_list))
        return count_words(subreddit, word_list, after)
    else:
        print('java: \njavascript: \npython: \nscala: \n')
