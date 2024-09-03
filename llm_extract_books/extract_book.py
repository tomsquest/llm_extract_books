from enum import Enum

from baml_py.baml_py import ClientRegistry

from baml_client import b
from baml_client.types import Book


class Model(str, Enum):
    ClaudeHaiku = "ClaudeHaiku"
    ClaudeSonnet = "ClaudeSonnet"
    GeminiFlash = "GeminiFlash"
    GeminiPro = "GeminiPro"


def extract_book(book_text: str, model: Model) -> Book:
    client_registry = ClientRegistry()
    client_registry.set_primary(model)
    book = b.ExtractBook(book_text, {"client_registry": client_registry})
    return book
