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
    print(f"Found {num_words} total words")

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

def get_book_report(book,char_list):

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(book)
    print("--------- Character Count -------")

    sd = sorted(char_list.items())
    
    for k,v in sd:
       
        if k.isalpha():
            print (f"{k}: {v}")

    print("============= END ===============")

pass