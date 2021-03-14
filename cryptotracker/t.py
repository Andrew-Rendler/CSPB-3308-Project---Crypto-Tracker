URL_FRAGMENT = "https://min-api.cryptocompare.com/data/v2/"
CRYPTOCOMPARE_ENDPOINTS = {
    "historical_daily": URL_FRAGMENT
    + "histoday?fsym={coin}&&tsym={currency}&limit={num_days}",
    "news": {
        "latest_news": URL_FRAGMENT + "news/?lang=EN",
        "latest_news_with_feeds": URL_FRAGMENT + "news/?lang=EN" + "&feeds={feeds}",
        "latest_news_with_categories": URL_FRAGMENT
        + "news/?lang=EN"
        + "&categories={categories}",
        "latest_news_after_timestamp": URL_FRAGMENT + "news/?lang=EN" + "&lTs={lTs}",
    },
}


def _iter_dict(tokens, dictionary):
    if len(tokens) == 1:
        return dictionary[tokens[0]]
    for key, value in dictionary.items():
        if key == tokens[0]:
            del tokens[0]
            return _iter_dict(tokens, value)


def clean_endpoints_string(endpoint):
    tokens = endpoint.split("+")
    print(_iter_dict(tokens, CRYPTOCOMPARE_ENDPOINTS))


endpoint = clean_endpoints_string("news+latest_news")