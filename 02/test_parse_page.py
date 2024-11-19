from solution import parse_page  # pylint: disable=E0611


def test_parse_page_empty_page():
    html = """<div id="mw-pages">
    </div>
    """
    beast_counts, next_page_url = parse_page(html)

    assert beast_counts == {}
    assert next_page_url is None


def test_parse_page_no_next_page(html_no_next_page):
    beast_counts, next_page_url = parse_page(html_no_next_page)

    assert beast_counts == {"А": 2, "Б": 1}
    assert next_page_url is None


def test_parse_page_with_next_page_link(html_next_page):
    beast_counts, next_page_url = parse_page(html_next_page)

    assert beast_counts == {"А": 2, "Б": 1}
    assert next_page_url == "https://ru.wikipedia.org/next_page"
