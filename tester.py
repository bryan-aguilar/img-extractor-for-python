import praw
import pprint
reddit = praw.Reddit(client_id='oFIVlnHQfgXjYQ',
                     client_secret='xt6o0AWVDm23ytFkZaav4L-sKZc',
                     user_agent='imgextract 1.0 /u/forrealbro')
earth_porn_sr = reddit.subreddit('EarthPorn')
x = []
for submission in earth_porn_sr.top(limit=5):
    x.append(submission)
for i in x:
    print(i.title)