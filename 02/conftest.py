import pytest


@pytest.fixture
def html_next_page():
    return """<div id="mw-pages">
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


@pytest.fixture
def html_no_next_page():
    return """<div id="mw-pages">
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
