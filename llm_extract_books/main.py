import json
from datetime import datetime

from llm_extract_books.extract_book import Model, extract_book
from llm_extract_books.get_books import get_all_books
from rich import print

from baml_client.types import Book


def main():
    print("Starting...")

    model = Model.ClaudeHaiku
    print(f"### Using {model}")

    results_file = f"outputs/{datetime.now().isoformat()}.{model.name}.all_books.jsonl"

    for index, book_text in enumerate(get_all_books()):
        print("########### Book", index)

        print("Text:")
        print("------------------------")
        print(book_text)
        print("------------------------")

        book = extract_book(book_text, model)

        print("Book:")
        print("------------------------")
        print(book)
        print("------------------------")

        save_result(results_file, book_text, model, book)

    print("Results saved to", results_file)
    print("Done.")


def save_result(file: str, book_text: str, model: Model, book: Book):
    with open(file, "a") as f:
        json.dump(
            {
                "model": model.name,
                "text": book_text.splitlines(),
                "book": book.model_dump(),
            },
            f,
        )
        f.write("\n")


if __name__ == "__main__":
    main()
