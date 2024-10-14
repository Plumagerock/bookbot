def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print (text)
    print (f"{word_count} words")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    book = path.split()
    return len(book)

main()
