class Book {
  title string
  series string?
  authors string[]
  rating int?
  volume string? @description("format as x/y if possible")
  comment string?
  date string? @description("format as yyyy-mm if possible")
  urls string[]
  fiction bool
}

function ExtractBook(book_text: string) -> Book {
  // client GeminiFlash
  client ClaudeHaiku

  prompt #"
    Your task is to extract structured information from the book and format it as JSON.

    Book:
    ---
    {{ book_text }}
    ---

    {# special macro to print the output instructions. #}
    {{ ctx.output_format }}

    JSON:
  "#
}

test Test_complete {
  functions [ExtractBook]
  args {
    book_text #"
      Les feux de Cibola - The Expanse - Tome 4/7 - James S.A. Corey
      Lu en avril 2024
      4 sur 5
      Je prends assez de plaisir à lire la suite de l'évolution du monde de The Expanse.
      Le héros est un peu comme Harry Potter, mais ca passe.
      [Roubaix](http://www.mediathequederoubaix.fr/ark:/245243523452)
      [Amazon](https://www.amazon.fr/Quality-Land-Marc-Uwe-Kling/dp/13414321)
    "#
  }
}

test Test_mini {
  functions [ExtractBook]
  args {
    book_text #"
      Garrett - Glen Cook
    "#
  }
}