def main():
    frankenstein = "books/frankenstein.txt"
    text = get_book_text(frankenstein)
    num_words = word_count(text)
    char_count = count_characters(text)
    print(char_count)

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
            char_count[character] = char_count[character] + 1
        else:
            char_count[character] = 1

    return char_count
    
main()