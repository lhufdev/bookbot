from stats import get_book_character_count, get_book_word_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    book_word_count = get_book_word_count(book_text)
    book_character_counts = get_book_character_count(book_text)

    print(f"Found {book_word_count} total words")
    print(book_character_counts)


main()
