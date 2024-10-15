def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_chars_dict(book_text)
    print(char_count)
    sorted_char_count = get_chars_dict_to_sorted(char_count)

    print_report(book_path, word_count, sorted_char_count)
    
# returns input book text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# returns length of book in number of words
def get_word_count(book):
    word_count = book.split()
    return len(word_count)

# returns characters from book as dict
def get_chars_dict(book):
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

def get_chars_dict_to_sorted(chars_dict):
    chars_sorted = []
    for char in chars_dict:
        chars_sorted.append({"char": char, "num": chars_dict[char]})
    chars_sorted.sort(reverse=True, key=sort_on)
    return chars_sorted

def print_report(book, word, chars):
    print(f"--- Begin report of {book} ---")
    print(f"{word} words found in document.")
    print()
    for char in chars:
        if char["char"].isalpha():
            print(f"The {char['char']} character was found {char['num']} times.")
    print()
    print("--- End report ---")

def sort_on(d):
    return d["num"]

main()
