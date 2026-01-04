import sys
from stats import get_word_count, get_character_count, get_alpha_characters

def get_book_text(path):
    print(f"Analyzing book found at {path}...")
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    book = get_book_text(path)

    word_count = get_word_count(book)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    character_count = get_character_count(book)
    alpha_characters = get_alpha_characters(character_count)
    for char in alpha_characters:
        print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


main()