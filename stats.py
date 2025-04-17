def get_book_text(file_path):
    text = ""

    with open(file_path) as f:
        text = f.read()

    return text

def get_num_words(book):

    text = book
    words = []
    num_words = 0

    words = text.split()
    
    num_words = len(words)
    print(f"{num_words} words found in the document")

pass

def get_num_chars(book):

    text = book.lower()
    counted = {}

    for i in text:
        if i not in counted:
            counted[i] = 1
        else:
            counted[i] += 1
            
    return counted