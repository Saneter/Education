# Travis Jarratt
# CIS 1600 - Assignment 2
# BMI Calculator with statements and categories using loops


# Initial input of height and weight.
height = int(input("Please Enter your height in inches: "))
weight = int(input("Please enter your weight in pounds: "))
# Calculation of BMI
bmi = 703 * (weight / height ** 2)
# Initial run of first data into categories
if bmi < 16:
    print("Your Body Mass Index is ", format(bmi))
    print("Your BMI category is Severe Thinness.")

elif 16 > bmi < 17:
    print("Your Body Mass Index is ", format(bmi))
    print("Your BMI category is Moderate Thinness.")

elif 17 > bmi < 18.4:
    print("Your Body Mass Index is ", format(bmi))
    print("Your BMI category is Mild Thinness.")

elif 18.5 > bmi < 25:
    print("Your Body Mass Index is ", format(bmi))
    print("Your BMI category is Normal.")

elif 25 > bmi < 30:
    print("Your Body Mass Index is ", format(bmi))
    print("Your BMI category is Overweight.")

elif 30 > bmi < 35:
    print("Your Body Mass Index is ", format(bmi))
    print("Your BMI category is Obese Class I.")

elif 35 > bmi < 41:
    print("Your Body Mass Index is ", format(bmi))
    print("Your BMI category is Obese Class II.")

elif bmi > 40:
    print("Your Body Mass Index is ", format(bmi))
    print("Your BMI category is Obese Class III.")

# Request for user input for continuance or ending the program
again = input("Please enter 'y' or 'Y' to continue or enter any other key to end.")
# While statement that will continue till any key but y or Y is entered.
while again == "y" or again == "Y":
    height = int(input("Please Enter your height in inches: "))
    weight = int(input("Please enter your weight in pounds: "))

    bmi = 703 * (weight / (height * height))

    if bmi < 16:
        print("Your Body Mass Index is ", format(bmi))
        print("Your BMI category is Severe Thinness.")

    elif 16 > bmi < 18.5:
        print("Your Body Mass Index is ", format(bmi))
        print("Your BMI category is Moderate Thinness.")

    elif 17 > bmi < 18.4:
        print("Your Body Mass Index is ", format(bmi))
        print("Your BMI category is Mild Thinness.")

    elif 18.5 > bmi < 25:
        print("Your Body Mass Index is ", format(bmi))
        print("Your BMI category is Normal.")

    elif 25 > bmi < 30:
        print("Your Body Mass Index is ", format(bmi))
        print("Your BMI category is Overweight.")

    elif 30 > bmi < 35:
        print("Your Body Mass Index is ", format(bmi))
        print("Your BMI category is Obese Class I.")

    elif 35 > bmi < 41:
        print("Your Body Mass Index is ", format(bmi))
        print("Your BMI category is Moderate Thinness.")

    elif bmi > 40:
        print("Your Body Mass Index is ", format(bmi))
        print("Your BMI category is Moderate Thinness.")

    again = input("Please enter 'y' or 'Y' to continue or enter any other key to end.")

# Ending statement
print("Thank you, Goodbye!")
