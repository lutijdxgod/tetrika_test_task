from solution import parse_page


def test_parse_page_empty_page():
    html = """<div id="mw-pages">
    </div>
    """
    beast_counts, next_page_url = parse_page(html)

    assert beast_counts == {}
    assert next_page_url == None


def test_parse_page_no_next_page():
    html = """<div id="mw-pages">
        <div class="mw-category-group">
            <h3>А</h3>
            <ul>
                <li>Антилопа</li>
                <li>Акула</li>
            </ul>
        </div>
        <div class="mw-category-group">
            <h3>Б</h3>
            <ul>
                <li>Бегемот</li>
            </ul>
        </div>
    </div>
    """
    beast_counts, next_page_url = parse_page(html)

    assert beast_counts == {"А": 2, "Б": 1}
    assert next_page_url == None


def test_parse_page_with_next_page_link():
    html = """<div id="mw-pages">
        <a href="/next_page" title="Категория:Животные по алфавиту">Следующая страница</a>
        <div class="mw-category-group">
            <h3>А</h3>
            <ul>
                <li>Антилопа</li>
                <li>Акула</li>
            </ul>
        </div>
        <div class="mw-category-group">
            <h3>Б</h3>
            <ul>
                <li>Бегемот</li>
            </ul>
        </div>
    </div>
    """
    beast_counts, next_page_url = parse_page(html)

    assert beast_counts == {"А": 2, "Б": 1}
    assert next_page_url == "https://ru.wikipedia.org/next_page"
