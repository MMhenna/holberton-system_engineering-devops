#!/usr/bin/python3
"""queries the Reddit API"""

import requests


def top_ten(subreddit):
    """returns first 10 posts"""
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    header = {"User-Agent": "mehdi"}
    params = {"limit": 10}

    response = requests.get(url, headers=header, params=params)

    if response.status_code == 404:
        print(None)

    for i in response.json().get("data").get("children"):
        print(i.get("data").get("title"))
