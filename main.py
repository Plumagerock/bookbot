def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print (text)
    print (f"{word_count} words")
    print(f"characters are: {char_count}")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(path):
    book = path.split()
    return len(book)

def get_char_count(book):
    chars = {}
    lower_book = book.lower()
    book_words = lower_book.split()
    for word in book_words:
        for char in word:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    
    return chars

main()
