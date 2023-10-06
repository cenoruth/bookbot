def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    chars_dict = get_book_chars(book_text)
    get_report(path, num_words, chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_chars(text):
    chars = {}
    file_words = text.lower()
    for char in set(file_words):
        chars[char] = file_words.count(char)
    return chars

def get_report(book, total_words, chars_dict):
    print(f"-- Begin report of {book} --")
    print(f"{total_words} found in the document\n")

    chars_list = [(k,v) for k,v in chars_dict.items()]
    chars_list.sort()

    for char, num in chars_list:
        if char.isalpha():
            print(f"The '{char}' character was found {num} times")

    print("-- End report --")

main()