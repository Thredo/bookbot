import string

def main():
    with open("books/Frankestein.txt") as f:
        file_contents = f.read()
        words_lst = text_to_words_list(file_contents)
        total_words = len(words_lst)
        amount_of_letters = letter_counter(file_contents.lower())
        word_and_count = most_used_word(words_lst)
        print_report(amount_of_letters, total_words, word_and_count)

def print_report(letters_dict, words, word_and_count):
    '''
        Prints data about the book to the console.

        Args:
            -letters_dict (dict): Dictionary with a letter (string) and the amount of times it appeared on the text (int)
            -words (int): The amount of words in the text
            -word_and_count (dict): Dictionary with the most used word (sttring) and the amount of times it appeared on the text (int)
    '''

    print("--- Begin report of the book --- \n ")
    print(f"There are a total of {words} words in the book \n ")
    print(f"The most used word is: '{word_and_count["word"]}' used {word_and_count["counter"]} times \n ")
    print("The amount of times a letter appears on the book by descending order:")
    sort_lst = sorted_dict(letters_dict)
    for l,v in sort_lst:
        print(f"The letter {l} appeared {v} Times.")
    print("--- End report ---")


def sorted_dict(letter_dict):
    '''
        Sorts a dictionary of words in descending order based on the times it was repeated on the text.

        Args:
            -letter_dict (dict): Dictionary of letters as keys and counter as value

        Return:
            list: sorted tuple of letter and counter pair

    '''
    return sorted(letter_dict.items(), key=lambda x :x[1], reverse=True)

def most_used_word(word_lst):
    '''
        Finds the most used word in the text

        Args:
            -word_lst (list): a list of words

        Return:
            dict: Dictionary with the most used word and its counter
    '''
    word_dict= {}

    for word in word_lst:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    most_used_word = {"word":"", "counter":0}

    for word, count in word_dict.items():
        if count > most_used_word['counter']:
            most_used_word['word'] = word
            most_used_word['counter'] = count

    return most_used_word


def letter_counter(text):
    '''
        Counts the amount of times a letter appears on the text

        Arg:
            -text (string): a text or book
        
        Return:
            dict: Dictionary with the letters used and their respective counter
    '''
    letters = {char: 0 for char in string.ascii_lowercase}
    
    for letter in text:
        if letter in letters:
            letters[letter] += 1

    return letters

def text_to_words_list(text):
    '''
        Receives the text and returns a list of words

        Arg:
            -text (string): a text or book
        
        Return:
            list: List containing all the words in the text
    '''
    ret_list = text.split()
    return ret_list





main()