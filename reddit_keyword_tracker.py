import praw 
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt


#---Reddit API Credentials
reddit = praw.Reddit(
    client_id="UImSQxkPPCrv4wpCGB1a3w",
    client_secret="0Rxrc2kJ7HZ9jAYiePtdM0NcPRNw1w",
    user_agent="trace"
)

#---User-defined inputs
subreddits = ["SkincareAddiction", "Frugal", "BuyItForLife"]
keywords = ["cerave", "olipop", "glossier", "birkenstock", "casper"]

#---Scrape latest posts
posts = []
for sub in subreddits:
    for post in reddit.subreddit(sub).new(limit=300):
        posts.append(post.title.lower() + " " + post.selftext.lower())

#---Count keyword mentions
counter = Counter()
for kw in keywords:
    counter[kw] = sum(kw in post for post in posts)

#---Output results
df = pd.DataFrame(counter.items(), columns=["Keyword", "Mentions"])
df = df.sort_values(by="Mentions", ascending=False)

df.to_csv("reddit_mentions.csv", index=False)

#---Plot
df.plot(kind="bar", x="Keyword", y="Mentions", title="Keyword Mentions on Reddit", legend=False)
plt.tight_layout()
plt.savefig("reddit_mentions_chart.png")
plt.show()
