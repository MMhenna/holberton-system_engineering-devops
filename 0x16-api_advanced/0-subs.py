#!/usr/bin/python3
"""queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """returns total subs"""
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    header = {"User-Agent": "mehdi"}

    response = requests.get(url, headers=header)

    if response.status_code == 404:
        return 0

    result = response.json().get("data")
    return result.get("subscribers")
