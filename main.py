def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    num_words = word_count(text)
    char_count = count_characters(text)
    alph_count = filter_alph(char_count)
    sort_alph = sort_count(alph_count)
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document")
    for i in range(0, len(sort_alph)):
        char = sort_alph[i]['char']
        count = sort_alph[i]['count']
        print(f"The '{char}' was found {count} times")

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters(text):
    lowered_string = text.lower()
    char_count = {}

    for character in lowered_string:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1

    return char_count

def filter_alph(char_count):
    alph_count = {}
    for character in char_count:
        if character.isalpha():
            alph_count[character] = char_count[character]
        else:
            pass
    return alph_count

def sort_on(dict):
    return dict["count"]

def sort_count(dict):
    dict_list = []
    for i in dict:
        small_dict = {"char": i, "count": dict[i]}
        dict_list.append(small_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

    
main()