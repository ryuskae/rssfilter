# rssfilter

Simple utilities to build Bing News RSS URLs from a user-entered search term.

## Usage

Generate a Bing News RSS URL for a query. The query is URL encoded so that
spaces or non-ASCII characters do not break the feed URL.

```bash
python -m rssfilter.cli "open ai"
# prints: https://www.bing.com/news/search?q=open+ai&format=rss
```

## Tests

```bash
python -m pytest
```
