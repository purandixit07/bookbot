book_path = "bookbot/books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    sorted_list = char_dict_to_sorted_list(char_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_dict(text):   
    letters_dict = {}
    for i in text:
        lowered = i.lower()
        if lowered not in letters_dict:
            letters_dict[lowered] = 1
        else:
            letters_dict[lowered] += 1
    return letters_dict


def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        if char.isalpha():
            sorted_list.append({"char":char, "num":char_dict[char]})
    sorted_list.sort(key = lambda ele: ele["num"], reverse = True)
    return sorted_list



main()