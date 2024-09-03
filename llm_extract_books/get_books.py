import random
from functools import lru_cache
from typing import List
from rich import print


@lru_cache(maxsize=None)
def get_all_books() -> List[str]:
    with open("data/books.txt", "r") as f:
        books = [book.strip() for book in f.read().strip().split("\n\n")]

    return books


def get_random_books(n: int = 3) -> List[str]:
    books = get_all_books()
    random.shuffle(books)
    return books[:n]


def get_random_book() -> str:
    return get_random_books(1)[0]


if __name__ == "__main__":
    print("Number of books:", len(get_all_books()))
    print("Random books:")
    print(get_random_books(3))
