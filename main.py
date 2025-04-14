def get_book_text(file_path):
    text = ""
    words = []
    num_words = 0

    with open(file_path) as f:
        text = f.read()

    words = text.split()
    
    num_words = len(words)
    print(f"{num_words} words found in the document")

    pass

def main():
    get_book_text("books/frankenstein.txt")

main()