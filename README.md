# Reddit Keyword Tracker

Trace scrapes Reddit posts from specified subreddits and counts how often user-defined keywords appear. 
It outputs results to a CSV and generates a bar chart of keyword popularity.

## 🔧 Tech Stack
- Python
- PRAW (Reddit API)
- pandas
- matplotlib

## 🚀 How It Works
1. User defines subreddits and keywords in the script.
2. Script fetches 300 latest posts from each subreddit.
3. Counts keyword mentions across all post titles and texts.
4. Outputs:
   - `reddit_mentions.csv`: Table of keyword frequencies
   - `reddit_mentions_chart.png`: Bar chart visualization

## 📦 How to Run

1. Install dependencies:

```bash
pip install praw pandas matplotlib
```

2. Set up your Reddit API credentials at https://www.reddit.com/prefs/apps

3. Replace the placeholders in `reddit_keyword_tracker.py`:

```python
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_SECRET",
    user_agent="YOUR_USER_AGENT"
)
```

4. Run the script:

```bash
python reddit_keyword_tracker.py
```

## 📈 Sample Output

- `reddit_mentions.csv`: keyword count table
- `reddit_mentions_chart.png`: chart for easy visualization

## 🔧 Future Ideas

- Time-based trend tracking
- Scrape comments 
- Web frontend

