
"""
Author: name
Description
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


def grade_level(word_list):
    # TODO Use the functions above to return grade level
    # Look in section 4-5f in your book at the case study
    words = word_count(word_list)
    sentences = num_sentences(word_list)
    syllables = num_syllables(word_list)
    level = round(0.39 * (words / sentences) + 11.08 * \
                  (syllables / words) - 15.59)
    return level  # replace this with a return of a useful value


def flesch_index(word_list, word_string):
    # TODO Use the functions above to return the flesch index
    # Look in section 4-5f in your book at the case study
    words = word_count(word_list)
    sentences = num_sentences(word_string)
    syllables = num_syllables(word_list)
    index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
    return index  # replace this with a return of a useful value


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
    elif metric == "fleish-index":
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
    # TODO use sets to return all the unique words
    # should return words that are in chunk 1 but not in chunk 2 and
    # those that are in chunk 2 but not in chunk 1
    pass


def get_file_string():
    # This function is complete
    fname = input("Enter the filename of the first file\n")
    if not os.path.isfile(fname):
        print("Invalid filename")
        # return None to indicated this did not work
        return None
    return open(fname).read()


def run_analysis():
    # TODO you have work to do to finish this function
    print("Welcome to the text analysis program")

    while True:
        print("Here are your options:")
        print("1. Compare two pieces of text")
        print("2. Fetch words that have occurred in two pieces of text")
        print("3. Fetch words that have occurred in only one of two pieces of text")
        print("0. Quit")
        choice = int(input("Please enter an option:"))
        if choice == 0:
            print("Good bye")
            return
        else:
            # get the file data from user
            file1_string = get_file_string()
            if file1_string is None:
                continue  # go back and start UI over
            file2_string = get_file_string()
            if file2_string is None:
                continue  # go back and start UI over

            print(num_sentences(file1_string))
            print(num_sentences(file2_string))

            if choice == 1:  # compare two pieces of text
                print("\nFile Comparison")
                value = compare_text(file1_string, file2_string, "size")
                if value == 0:
                    print("The files have the same number of words")
                elif value > 0:
                    print("The first file has more words than the second does")
                else:
                    print("The second file has more words than the first does")

                #value = compare_text(file1_string, file2_string, "density")
                # TODO add code to nicely tell the user what the comparison means
                print("value")

                # TODO get results for Grade Level and print them nicely
                #value = compare_text(file1_string, file2_string, "grade-level")
                print("value")

                # TODO get results for Fleish Index and print them nicely
                value = compare_text(file1_string, file2_string, "fleish-index")
                print(value)

                print("\n\n")
            elif choice == 2:
                common_words = fetch_common_words(file1_string, file2_string)
                print("\nThe two files have these words in common")
                print(common_words)
                print("\n\n")
            elif choice == 3:
                unique_words = fetch_unique_words(file1_string, file2_string)
                print(unique_words)

            else:
                pass
    return


# main
if __name__ == '__main__':
    run_analysis()
