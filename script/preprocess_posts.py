import numpy as np
import pandas as pd
import re

# create dataframe, transform timestamps
post_data = pd.read_csv('../data/reddit_wsb.csv')
post_data = post_data[pd.to_datetime(post_data.timestamp).dt.year >= 2021]

posts = post_data[['id', 'title', 'body', 'timestamp']].copy().dropna()
posts.title = posts.title.str.lower()

# remove URLs
posts.title = posts.title.apply(lambda x: re.sub(r'@[^\s]+', '', x))
posts.body = posts.body.apply(lambda x: re.sub(r'@[^\s]+', '', x))

# remove time from timestamp
# posts.timestamp = pd.to_datetime(posts.timestamp).dt.date

# filter for gme mentions
search_pattern = r'\bgme\b'
posts = posts[(posts.title.str.contains(r'\bgme\b')) | posts.body.str.contains(r'\bgme\b')]


print(posts.shape)