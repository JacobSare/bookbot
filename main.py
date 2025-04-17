from stats import get_book_text
from stats import get_num_words
from stats import get_num_chars

def main():
    char_list = {}

    text  = get_book_text("books/frankenstein.txt")

    get_num_words(text)
    char_list = get_num_chars(text)
    print(char_list)

main()