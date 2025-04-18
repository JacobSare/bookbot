import sys

from stats import get_book_text
from stats import get_num_words
from stats import get_num_chars
from stats import get_book_report

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_loc = sys.argv[1]

    char_list = {}

    text  = get_book_text(book_loc)

    char_list = get_num_chars(text)

    get_book_report(text,char_list)
    

main()