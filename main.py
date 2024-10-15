# Bookbot project from Boot.dev
#
# Created by:   Ian Featherstone
# Version:      1
#

def main():
    # frankenstein file located here: https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_chars_dict(book_text)
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

# returns characters from book as dict (converted to all lowercase)
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

# returns list of sorted characters in format {char: num}
def get_chars_dict_to_sorted(chars_dict):
    chars_sorted = []
    for char in chars_dict:
        chars_sorted.append({"char": char, "num": chars_dict[char]})
    chars_sorted.sort(reverse=True, key=sort_key)
    return chars_sorted

# prints report of book, word count, character freq
def print_report(book, word, chars):
    print(f"--- Begin report of {book} ---")
    print()
    print(f"{word} words found in document.")
    print()
    for char in chars:
        if char["char"].isalpha():
            print(f"The {char['char']} character was found {char['num']} times.")
    print()
    print("--- End report ---")

# return sort key by num
def sort_key(d):
    return d["num"]

main()
