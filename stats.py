def count_words(book):
    # count the words in the string
    word_list = book.split()
    word_count = len(word_list)
    return f"Found {word_count} total words"

def count_characters(book):
    lower_case = book.lower()
    characters = {}
    # count the characters in the string and add them to the dictionary
    for char in lower_case:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    # print the results
    return characters

def char_counts_list(total_characters):
    # create an empty list
    char_counts = []
    # loop through the results of count_characters
    # create a new dictionary for each character
    # append each dictionary to the char_counts list
    for item in total_characters:
        char_dict = {}
        key = "character"
        value = "number"
        char = item
        count = total_characters[char]
        char_dict[key] = char
        char_dict[value] = count
        char_counts.append(char_dict)
    return char_counts

def sort_on(char_counts_list):
    return char_counts_list["number"]

