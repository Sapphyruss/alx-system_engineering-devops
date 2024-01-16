#!/usr/bin/python3
"""Query the Reddit API and returns a list of all hot titles"""
import requests


def count_words(subreddit, word_list, count=None, after=None):
    """queries the Reddit API and returns a list of all hot titles"""
    if count is None:
        count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    header = {'User-agent': 'redditapi'}
    if after:
        url += f"&after={after}"
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']

    if not posts:
        return count
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
    after = data['data']['after']
    if after:
        return count_words(subreddit, word_list, count, after)
    sort_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sort_count:
        print(f"{key}: {value}")
