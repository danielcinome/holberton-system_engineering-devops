#!/usr/bin/python3
""" Request Reddit API """
import requests

def number_of_subscribers(subreddit):
    """ numbers of subs """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    tok = {'user-agent': 'X-Modhash'}
    req = requests.get(url, headers=tok)
    if req.history or req.status_code == 404:
       return 0
    else:
       req = req.json()
       return req.get('data').get('subscribers')
