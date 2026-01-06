import pytest

from rssfilter.bing import build_bing_news_rss_url


def test_builds_encoded_url_from_query_with_spaces():
    assert build_bing_news_rss_url("open ai") == (
        "https://www.bing.com/news/search?q=open+ai&format=rss"
    )


def test_builds_encoded_url_from_query_with_non_ascii():
    assert build_bing_news_rss_url("서울 뉴스") == (
        "https://www.bing.com/news/search?q=%EC%84%9C%EC%9A%B8+%EB%89%B4%EC%8A%A4&format=rss"
    )


def test_empty_query_is_rejected():
    with pytest.raises(ValueError):
        build_bing_news_rss_url("   ")
