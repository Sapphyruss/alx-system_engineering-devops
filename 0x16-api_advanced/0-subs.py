#!/usr/bin/python3
"""Query the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    header = {'User-agent': 'ALX project'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json()
    return data['data']["subscribers"]
