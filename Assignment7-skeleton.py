"""
Author: Travis Jarratt
CIS 1600 - Assignment 7
Saint Louis University
A program to analyze test files using the Flesch scale.
Will take two files as inputs and output various results
based on user choices.
"""

from functools import reduce
import os


def num_sentences(textStr):
    # This function is complete
    # Pass in a string, not a list
    sentences = textStr.count('.') + textStr.count('?') + \
                textStr.count(':') + textStr.count(';') + \
                textStr.count('!')
    return sentences


def num_syllables(word_list):
    # This function is complete
    # Pass in a list of words. This function is complete
    # Count the syllables
    no_syllables = 0
    vowels = "aeiouAEIOU"
    for word in word_list:
        for vowel in vowels:
            no_syllables += word.count(vowel)
        for ending in ['es', 'ed', 'e']:
            if word.endswith(ending):
                no_syllables -= 1
        if word.endswith('le'):
            no_syllables += 1
    return no_syllables


def word_count(word_list):
    # This function is complete
    return len(word_list)


def grade_level(word_list, word_string):
    # Computes Grade level
    words = word_count(word_list)
    sentences = num_sentences(word_string)
    syllables = num_syllables(word_list)
    level = int(round(0.39 * (words / sentences) + 11.8 *
                      (syllables / words) - 15.59))
    return level


def flesch_index(word_list, word_string):
    # Computes the Flesch Index
    words = word_count(word_list)
    sentences = num_sentences(word_string)
    syllables = num_syllables(word_list)
    index = 206.835 - 1.015 * (words / sentences) - \
            84.6 * (syllables / words)
    return index


def get_word_list_from_string(mystring):
    # get rid of special characters by replacing them with spaces
    for character in "\n\t.,?:;!":
        mystring = mystring.replace(character, " ")
    # break the string into words based on the spaces
    wordlist = list(map(lambda word: word.strip(), mystring.split(" ")))

    # get rid of empty strings.  Multiple spaces in a row can cause this.
    wordlist = list(filter(lambda word: len(word) > 0, wordlist))
    return wordlist


def compare_text(wordstring1, wordstring2, metric):
    ## returns a value < 0 if chunk 2 is better than chunk1 according to the metric
    ## returns a value > 0  if chunk1 is better than chunk2 and 0 is they are both equal

    val = -99
    wordlist1 = get_word_list_from_string(wordstring1)
    wordlist2 = get_word_list_from_string(wordstring2)

    if metric == "size":
        val = len(wordlist1) - len(wordlist2)
    elif metric == "density":
        # Note: Density is the average letters per word
        c1 = len(reduce(lambda a, b: a + b, wordlist1)) / len(wordlist1)
        c2 = len(reduce(lambda a, b: a + b, wordlist2)) / len(wordlist2)
        val = c1 - c2
    # add other metrics here
    elif metric == "grade-level":
        c1 = grade_level(wordlist1, wordstring1)
        c2 = grade_level(wordlist2, wordstring2)
        val = c1 - c2
    elif metric == "flesch-index":
        c1 = flesch_index(wordlist1, wordstring1)
        c2 = flesch_index(wordlist2, wordstring2)
        val = c1 - c2
    return val


def fetch_common_words(word_string1, word_string2):
    wordlist1 = get_word_list_from_string(word_string1)
    wordlist2 = get_word_list_from_string(word_string2)
    set1 = set(wordlist1)
    set2 = set(wordlist2)
    return set1.intersection(set2)


def fetch_unique_words(word_string1, word_string2):
    # should return words that are in chunk 1 but not in chunk 2 and
    # those that are in chunk 2 but not in chunk 1
    word_list1 = get_word_list_from_string(word_string1)
    word_list2 = get_word_list_from_string(word_string2)
    word_set1 = set(word_list1)
    word_set2 = set(word_list2)
    common_set = word_set1 & word_set2
    joint_set = word_set1 | word_set2
    joint_set.difference_update(common_set)
    return joint_set


def get_file_string():
    # This function is complete
    fname = input("Enter the filename of the file\n")
    if not os.path.isfile(fname):
        print("Invalid filename")
        # return None to indicated this did not work
        return None
    return open(fname).read()


def run_analysis():
    print("Welcome to the text analysis program.")

    while True:
        print("Here are your options:\n")
        print("1. Load text files")
        print("2. Compare two pieces of text")
        print("3. Fetch words that have occurred in two pieces of text")
        print("4. Fetch words that have occurred in only one of two pieces of text")
        print("0. Quit")
        choice = int(input("Please enter an option: \n"))
        if choice == 0:
            print("Good bye")
            exit()
        elif choice == 1:
            # get the file data from user
            file1_string = get_file_string()
            if file1_string is None:
                continue  # go back and start UI over
            file2_string = get_file_string()
            if file2_string is None:
                continue  # go back and start UI over
        elif choice == 2:  # compare two pieces of text
            try:
                value = compare_text(file1_string, file2_string, "size")
                print("\nFile Comparison")
                if value == 0:
                    print("The files have the same number of words")
                elif value > 0:
                    print("The first file has more words than the second does")
                else:
                    print("The second file has more words than the first does")

                value = compare_text(file1_string, file2_string, "density")
                if value == 0:
                    print("The files have the same density")
                elif value > 0:
                    print("The first file has greater density than the second does")
                else:
                    print("The second file has greater density than the first does")

                value = compare_text(file1_string, file2_string, "grade-level")
                if value == 0:
                    print("The files have the same grade level")
                elif value > 0:
                    print("The first file has a higher grade level than the second does")
                else:
                    print("The second file has higher grade level than the first does")

                value = compare_text(file1_string, file2_string, "flesch-index")
                if value == 0:
                    print("The files have the same Flesch Index level.")
                elif value > 0:
                    print("The second file has a lower Flesch Index level \n"
                          "and is harder to read than the first.")
                else:
                    print("The first file has a lower Flesch Index level \n"
                          "and is harder to read than the second.")
            except UnboundLocalError:
                print("You must enter files before doing this option.\n")
                return run_analysis()

            print("\n\n")
        elif choice == 3:
            try:
                common_words = fetch_common_words(file1_string, file2_string)
                print("\nThe two files have these words in common")
                print(common_words)
                print("\n\n")
            except UnboundLocalError:
                print("You must enter files before doing this option.\n")
                return run_analysis()
        elif choice == 4:
            try:
                unique_words = fetch_unique_words(file1_string, file2_string)
                print("The unique words from both files are:")
                for word in unique_words:
                    print("{}".format(word))
                print("\n\n")
            except UnboundLocalError:
                print("You must enter files before doing this option.\n")
                return run_analysis()

        else:
            pass
    return


# main
if __name__ == '__main__':
    run_analysis()
