def get_book_text(filepath):
    # open the file and read it as a string
    with open(filepath) as f:
        frankenstein = f.read()
    return frankenstein

def main():
    # import functions from other .py files
    import sys
    from stats import count_words
    from stats import count_characters
    from stats import char_counts_list
    from stats import sort_on

    # make sure there are 2 arguments in sys.argv
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        # declare a variable and set the path to the file
        filepath = sys.argv[1]
    
    # call get_book_text and get the results
    book = get_book_text(filepath)
    
    # call count_words and get the results
    total_words = count_words(book)
    
    # call count_characters and get the results
    total_characters = count_characters(book)
    
    # call and sort the char_counts_list highest to lowest
    char_list = char_counts_list(total_characters)
    char_list.sort(reverse=True, key=sort_on)
    
    # print the report
    header = "============ BOOKBOT ============\n\n"
    process = f"Analyzing book found at {filepath}...\n\n"
    count_header = "----------- Word Count ----------\n\n"
    total = f"{total_words}\n\n"
    char_count_header = "--------- Character Count -------\n"
    report_start = header + process + count_header + total + char_count_header
    print(report_start)
    # loop through the char_list to print 
    for item in char_list:
        letter = f"{item['character']}"
        count = f": {item['number']}\n"
        if letter.isalpha():
            print(letter + count)
    footer = "============= END ==============="
    print(footer)

main()