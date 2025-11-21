from stats import (
    get_book_character_count,
    get_book_word_count,
    get_sorted_character_counts,
)

FILE_PATH = "books/frankenstein.txt"


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_sorted_character_counts(sorted_character_counts):
    for item in sorted_character_counts:
        if item["char"].isalpha():
            char = item["char"]
            count = item["num"]
            print(f"{char}: {count}")


def main():
    book_text = get_book_text(FILE_PATH)
    book_word_count = get_book_word_count(book_text)
    book_character_counts = get_book_character_count(book_text)
    sorted_character_counts = get_sorted_character_counts(book_character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {FILE_PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    print_sorted_character_counts(sorted_character_counts)
    print("============= END ===============")


main()
