"""Helpers for Bing News RSS generation."""
from urllib.parse import quote_plus


def build_bing_news_rss_url(query: str) -> str:
    """Return a Bing News RSS URL for the provided search query.

    Bing requires the query to be URL encoded. Previously queries were
    concatenated directly, which broke when spaces or non-ASCII characters
    were present and resulted in Bing responding with an HTML page instead of
    an RSS feed. Normalizing and encoding the query ensures a valid RSS URL.

    Args:
        query: Search text entered by the user.

    Returns:
        A fully-qualified Bing News RSS URL.

    Raises:
        ValueError: If ``query`` is empty or only whitespace.
    """

    normalized = query.strip()
    if not normalized:
        raise ValueError("search query must not be empty")

    encoded_query = quote_plus(normalized)
    return f"https://www.bing.com/news/search?q={encoded_query}&format=rss"
