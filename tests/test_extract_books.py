from llm_extract_books.extract_book import Model, extract_book
from baml_client.types import Book

model = Model.ClaudeHaiku
# model = Model.GeminiPro


def test_minimal() -> None:
    book_text = """
        Garrett - Glen Cook
    """

    book = extract_book(book_text, model)

    assert book == Book(title="Garrett", authors=["Glen Cook"], urls=[], fiction=True)


def test_complete() -> None:
    book_text = """
      Quality Land - Tome 1/2 - Marc-Uwe Kling
      Lu en avril 2024
      4 sur 5
      Vraiment bien, drole, perspicace, et écrit avant GPT !
      [Roubaix](http://www.mediathequederoubaix.fr/ark:/20179/KH339866)
      [Amazon](https://www.amazon.fr/Quality-Land-Marc-Uwe-Kling/dp/2330153171)
    """

    book = extract_book(book_text, model)

    assert book == Book(
        title="Quality Land",
        series=None,
        authors=["Marc-Uwe Kling"],
        rating=4,
        volume="1/2",
        comment="Vraiment bien, drole, perspicace, et écrit avant GPT !",
        date="2024-04",
        urls=[
            "http://www.mediathequederoubaix.fr/ark:/20179/KH339866",
            "https://www.amazon.fr/Quality-Land-Marc-Uwe-Kling/dp/2330153171",
        ],
        fiction=True,
    )
