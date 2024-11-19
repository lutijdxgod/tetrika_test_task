import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://ru.wikipedia.org"
LETTERS = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ"


def fetch_page(url: str) -> str:
    """Fetch a URL and return it's contents."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.text


def parse_page(text: str) -> tuple[dict[str, int], str | None]:
    """Parse an html page to find beast count."""
    soup = BeautifulSoup(text, "html.parser")
    pages_with_beasts = soup.find("div", attrs={"id": "mw-pages"})
    if not pages_with_beasts:
        return {}, None

    beast_count = {}
    beast_pages_by_first_letter = pages_with_beasts.find_all(
        "div", class_="mw-category-group"
    )
    for letter_entry in beast_pages_by_first_letter:
        letter = letter_entry.find("h3").text
        beasts_on_page = letter_entry.find_all("li")
        beasts_on_page_count = len(beasts_on_page)
        beast_count[letter] = beasts_on_page_count

    next_page_url = None
    next_page = soup.find("a", string="Следующая страница")
    if next_page is not None:
        next_page_url = BASE_URL + next_page.attrs["href"]

    return beast_count, next_page_url


def write_to_csv(beast_count_dict: dict, filename: str = "beasts.csv"):
    """Write result dict to a csv file."""
    with open(filename, "w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["letter", "beast_count"])
        writer.writerows(beast_count_dict.items())


if __name__ == "__main__":
    total_beast_count = {letter: 0 for letter in LETTERS}
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"  # pylint: disable=C0103

    while url:
        fetched_text = fetch_page(url)
        beast_count_for_page, url = parse_page(text=fetched_text)

        for letter, count in beast_count_for_page.items():
            total_beast_count[letter] += count

    write_to_csv(beast_count_dict=total_beast_count)
