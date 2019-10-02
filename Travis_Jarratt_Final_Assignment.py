"""
Name: Travis Jarratt
Final Assignment for CIS 1600
Saint Louis University

This program takes in a CSV file with three fields (Days, Amounts, Category)
and displays the information to the user via text navigation in three formats:

The list as a whole.
User driven category.
Total by Day.
"""


def get_data(fname):
    fileObj = open(fname)
    lines = fileObj.readlines()
    expense_list = []

    for line in lines[1:]:  # for lines starting at 2 (excluding 1 because it is the
        line_items = line.strip().split(",")  # strip removes the newline character
        expense_list.append([line_items[0], line_items[1], line_items[2]])

    return expense_list


def print_expenses(expense_list):
    # Prints the expense list in ordered columns.
    print("{:<20s} {:<20s} {:<20s}".format("Days", "Amount", "Category"))
    print("{}".format("-" * 60))
    for item in expense_list:
        print("{:<20s} {:<20.2f} {:<20s}".format(item[0], float(item[1]), item[2]))


def category_filter(expense_list, user_choice):
    # Filters the expense list using users choice.
    for line in expense_list:
        if user_choice in line:
            print("{:<20s} {:<20.2f} {:<20s}".format(line[0], float(line[1]), line[2]))


def display_for_category(expense_list):
    # Takes user choice and shows expense category for that choice.
    print("Please enter a category selection using:\n"
          "{} For {}\n"
          "{} For {}\n"
          "{} For {}\n"
          "{} For {}\n"
          "{} For {}\n".format("'b' or 'B'", 'Beverages',
                               "'f' or 'F'", 'Food',
                               "'e' or 'E'", 'Entertainment',
                               "'t' or 'T'", 'Travel',
                               "'c' or 'C'", 'Clothing'))
    category_choice = input("Enter your choice here: ")
    if category_choice in ('b', 'B'):
        print("\nYou have selected Beverages.")
        print("{:<20s} {:<20s} {:<20s}".format("Days", "Amount", "Category"))
        print("{}".format("-" * 60))
        category_filter(expense_list, 'Beverages')
    elif category_choice in ('f', 'F'):
        print("\nYou have selected Food.")
        print("{:<20s} {:<20s} {:<20s}".format("Days", "Amount", "Category"))
        print("{}".format("-" * 60))
        category_filter(expense_list, 'Food')
    elif category_choice in ('e', 'E'):
        print("\nYou have selected Entertainment.")
        print("{:<20s} {:<20s} {:<20s}".format("Days", "Amount", "Category"))
        print("{}".format("-" * 60))
        category_filter(expense_list, 'Entertainment')
    elif category_choice in ('t', 'T'):
        print("\nYou have selected Travel.")
        print("{:<20s} {:<20s} {:<20s}".format("Days", "Amount", "Category"))
        print("{}".format("-" * 60))
        category_filter(expense_list, 'Travel')
    elif category_choice in ('c', 'C'):
        print("\nYou have selected Clothing.")
        print("{:<20s} {:<20s} {:<20s}".format("Days", "Amount", "Category"))
        print("{}".format("-" * 60))
        category_filter(expense_list, 'Clothing')
    else:
        print("That is an invalid choice. Please choose again:\n")
        return display_for_category(expense_list)
    print("\n\nWould you like to select another category?\n")
    stay_go = input("Please enter 'Yes' or 'No':\n")
    if stay_go in ("Yes", "yes", "Y", 'y'):
        return display_for_category(expense_list)
    else:
        pass


def summarize_by_weekday(expense_list):
    # Combines the amount spent each day into a total for all instances of that day.
    # Displays all days at once.
    mon_total = 0
    tue_total = 0
    wed_total = 0
    thu_total = 0
    fri_total = 0
    for line in expense_list:
        if "Monday" in line:
            mon_total += float(line[1])
        elif "Tuesday" in line:
            tue_total += float(line[1])
        elif "Wednesday" in line:
            wed_total += float(line[1])
        elif "Thursday" in line:
            thu_total += float(line[1])
        elif "Friday" in line:
            fri_total += float(line[1])
    print("\n\nThe Weekday Totals are:\n"
          "{:<10}  {:>10.2f}\n"
          "{:<10}  {:>10.2f}\n"
          "{:<10}  {:>10.2f}\n"
          "{:<10}  {:>10.2f}\n"
          "{:<10}  {:>10.2f}\n".format("Monday", mon_total,
                                       "Tuesday", tue_total,
                                       "Wednesday", wed_total,
                                       "Thursday", thu_total,
                                       "Friday", fri_total))


def run_ui(expenses):
    # Original UI modified for clarity.
    while True:
        print("\n\nPlease select an option below by entering a number: \n")
        choice = int(input("1 display all of the expense records\n"
                           "2 to display all of the expense records for a particular category\n"
                           "3 to display the total amount of money spent on each weekday, aggregated per day\n"
                           "0 to quit.\n"))
        if choice == 0:
            print("Good bye!")
            quit()
        elif choice == 1:
            print_expenses(expenses)
            continue
        elif choice == 2:
            display_for_category(expenses)
            continue
        elif choice == 3:
            summarize_by_weekday(expenses)
            continue
        else:
            print("Please enter a valid choice")


if __name__ == '__main__':
    expense_data = get_data("./expenses.csv")
    run_ui(expense_data)
