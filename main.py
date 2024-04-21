import string

def main():
    with open("books/Frankestein.txt") as f:
        file_contents = f.read()
        total_words = word_counter(file_contents)
        amount_of_letters = letter_counter(file_contents.lower())
        print_report(amount_of_letters, total_words)
        

def print_report(letters_dict, words, ):
    print("--- Begin report of the book --- \n ")
    print(f"There are a total of {words} words in the book \n ")
    print("The amount of times a letter appears on the book by descending order:")
    sort_lst = sorted_dict(letters_dict)
    for l,v in sort_lst:
        print(f"The letter {l} appeared {v} Times.")
    print("--- End report ---")


def sorted_dict(letter_dict):
    return sorted(letter_dict.items(), key=lambda x :x[1], reverse=True)




def letter_counter(text):
    letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
     'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    for letter in text:
        if letter in letters:
            letters[letter] += 1

    return letters

def word_counter(text):
    ret_list = text.split()
    return len(ret_list)





main()