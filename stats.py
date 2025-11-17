def get_book_word_count(book_text: str) -> int:
    return len(book_text.split())


def get_book_character_count(book_text: str) -> dict[str, int]:
    character_counts = {}
    for ch in book_text.lower():
        if ch not in character_counts:
            character_counts[ch] = 1
        else:
            character_counts[ch] += 1
    return character_counts
