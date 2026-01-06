"""Command line helpers for rssfilter."""
from argparse import ArgumentParser
from rssfilter import build_bing_news_rss_url


def main(argv: list[str] | None = None) -> int:
    parser = ArgumentParser(description="Build Bing News RSS URL from a search query")
    parser.add_argument("query", help="Search term to generate an RSS feed for")
    args = parser.parse_args(argv)

    rss_url = build_bing_news_rss_url(args.query)
    print(rss_url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
