import os
from functools import reduce

print(os.listdir("."))


def compare_text_chunks(chunk1, chunk2, metric):
    # returns a value < 0 if chunk 2 is better than chunk1 according to the metric
    # returns a value > 0  if chunk1 is better than chunk2 and 0 is they are both equal
    val = -99
    if metric == "size":
        val = len(chunk1) - len(chunk2)
    elif metric == "density":
        c1 = len(reduce(lambda a, b: a + b, chunk1)) / len(chunk1)
        c2 = len(reduce(lambda a, b: a + b, chunk2)) / len(chunk2)
        val = c1 - c2
    # add other metrics here
    return val


def fetch_common_words(chunk1, chunk2):
    set1 = set(chunk1)
    set2 = set(chunk2)
    return set1.intersection(set2)


def fetch_unique_words(chunk1, chunk2):
    # should return words that are in chunk 1 but not in chunk 2 and
    # those that are in chunk 2 but not in chunk 1
    pass


def fetch_text_chunk_from_file(fname):
    chunk = open(fname).read()
    chunk = list(map(lambda word: word.strip(), chunk.split(" ")))
    return chunk


def run_analysis():
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
        elif choice == 1:  # compare two pieces of text
            fname_1 = input("Enter the filename of the first file\n")

            if os.path.isfile(fname_1):
                fname_2 = input("Enter the filename of the second file\n")
                if os.path.isfile(fname_2):
                    chunk1 = fetch_text_chunk_from_file(fname_1)
                    chunk2 = fetch_text_chunk_from_file(fname_2)
                    outcome = compare_text_chunks(chunk1, chunk2, "density")
                    print("The result of comparison is: " + str(outcome))

                else:
                    print("The file whose name you have entered does not exist")
                    continue
            else:
                print("The file whose name you have entered does not exist")
                continue

        elif choice == 2:
            pass
        elif choice == 3:
            pass
        else:
            pass
    return


if __name__ == '__main__':
    run_analysis()
