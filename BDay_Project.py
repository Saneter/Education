import datetime
today = datetime.date.today()

def date_at_100(birthday):
    return today.year + years_to_100(birthday)

def years_to_100(birthday):
    age = age_calculator(birthday)
    difference = 100 - age
    return difference

def age_calculator(birthday):
    year, month, day = map(int, birthday.split('/'))
    date1 = datetime.date(year, month, day)
    age = today.year - date1.year - ((today.month, today.day) <(date1.month, date1.day))
    return age

def main():
    name = input("Please enter your name: ")
    birthday = input("Please enter your birthday in yyyy/mm/dd: ")
    print("Hello, {}. Today is {}".format(name, today))
    print("You are {} years old.".format(age_calculator(birthday)))
    print("You will be 100 years old in {} years".format(years_to_100(birthday)))
    print("In {}.".format(date_at_100(birthday)))


if __name__ == "__main__":
    main()