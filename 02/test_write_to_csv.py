import csv
from solution import write_to_csv  # pylint: disable=E0611


def test_write_to_csv():
    filename = "test.csv"
    beast_count = {"А": 2, "Б": 1}
    write_to_csv(beast_count, filename)

    with open(filename, encoding="UTF-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert rows == [["letter", "beast_count"], ["А", "2"], ["Б", "1"]]
