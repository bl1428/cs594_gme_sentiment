import numpy as np
import pandas as pd
import re

# create dataframe, transform timestamps
post_data = pd.read_csv('../data/reddit_wsb.csv')
post_data = post_data[pd.to_datetime(post_data.timestamp).dt.year >= 2021]
# print(post_data.head(3))

titles = post_data[['title', 'timestamp']].copy().dropna()
titles.title = titles.title.str.lower()
bodies = post_data[['body', 'timestamp']].copy().dropna()
bodies.body = bodies.body.str.lower()

# remove URLs
titles.title = titles.title.apply(lambda x: re.sub('@[^\s]+', '', x))
bodies.body = bodies.body.apply(lambda x: re.sub('@[^\s]+', '', x))

# remove time from timestamp
# titles.timestamp = pd.to_datetime(titles.timestamp).dt.date
# bodies.timestamp = pd.to_datetime(bodies.timestamp).dt.date