# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:17:48 2017

@author: Ivan
"""

from pprint import pprint
import requests
import json
import praw

reddit = praw.Reddit(client_id='sg4GZxrX9MLurA',client_secret='4tQ0jlPW8RhPGHNXtqe5pU72uj4',user_agent= 'Funnylaksa')

#print(reddit.user.me())
print(reddit.read_only)

#for submission in reddit.subreddit('learnpython').hot(limit=10):
#    print(submission.title)

submission = reddit.submission(url='https://www.reddit.com/r/funny/comments/3g1jfi/buttons/')

from praw.models import MoreComments
for top_level_comment in submission.comments:
    if isinstance(top_level_comment, MoreComments):
        continue
    print(top_level_comment.body)




