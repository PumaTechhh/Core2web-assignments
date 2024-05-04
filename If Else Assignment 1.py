'''Program 1: Write a Program to Find a Maximum between two numbers
Input: 1 2
Output: 2 is Max number between 1 & 2'''

a = 1
b = 2
if a > b:
    print(a,"is greater number")
elif b > a:
    print(b,"is max number between",a,"&",b) 
else:
    print("numbers are equal")

'''Program 2: Write a Program to check whether the number is Negative,
Positive or equal to Zero.
Input: -2
Output: -2 is the negative number'''

num = int(input("Input: "))
if num < 0:
    print(num,"is the negative number")
elif num == 0:
    print(num," equal to zero")
else:
    print(num,"is the positive number")

'''Program 3: Write a Program to Find whether the number Is Even or Odd
Input: 4
Output: 4 is an Even Number!'''

num = int(input("Input: "))

if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

'''Program 4: Write a Program to check whether the number is divisible by 5
or not.
Input: 55
Output: 55 is divisible by 5'''

num = int(input("Input: "))

if num % 5 == 0:
    print(num, "is divisible by 5")
else:
    print(num, "is not divisible by 5")

'''Program 5: Write a Program to take an integer ranging from 0 to 6 and print
corresponding weekday (week starting from Monday)
Input: 2
Output: Wednesday.'''

weekday = int(input("Input: "))

if weekday == 0:
    print("Monday")
elif weekday == 1:
    print("Tuesday")
elif weekday == 2:
    print("Wednesday")
elif weekday == 3:
    print("Thursday")
elif weekday == 4:
    print("Friday")
elif weekday == 5:
    print("Saturday")
elif weekday == 6:
    print("Sunday")
else:
    print("Invalid input. Please enter a number from 0 to 6.")

'''Program 6: Write a Program to check whether the Character is Alphabet or
not.
Input: v
Output: v is an alphabet.'''

char = input("Input: ")

if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
    print(char, "is an alphabet.")
else:
    print(char, "is not an alphabet.")

'''Program 7: Write a Program to take a number of months and print the number of
days in that month.
Input: 4
Output: April is a 30-day month.'''

month = int(input("Input: "))

if month == 1:
    print("January is a 31-day month.")
elif month == 2:
    print("February is a 28 or 29-day month.")
elif month == 3:
    print("March is a 31-day month.")
elif month == 4:
    print("April is a 30-day month.")
elif month == 5:
    print("May is a 31-day month.")
elif month == 6:
    print("June is a 30-day month.")
elif month == 7:
    print("July is a 31-day month.")
elif month == 8:
    print("August is a 31-day month.")
elif month == 9:
    print("September is a 30-day month.")
elif month == 10:
    print("October is a 31-day month.")
elif month == 11:
    print("November is a 30-day month.")
elif month == 12:
    print("December is a 31-day month.")
else:
    print("Invalid input. Please enter a number from 1 to 12.")

'''Program 8: Write a program to check whether the number is greater than 10 or
not
Input: 12
Output: yes 12 is greater than 10
Input: 2
Output: no 2 is less than 10'''

num = int(input("Input: "))

if num > 10:
    print("yes",num," is greater than 10")
else:
    print("no",num," is less than or equal to 10")

'''9. Program 9: Write a program to check whether the input character is a vowel or
consonant
Input: ‘a’
Output: vowel
Input: ‘b’
Output: consonant'''

char = input("Input: ")

if char in 'aeiouAEIOU':
    print("vowel")
else:
    print("consonant")

'''Program 10: WAP that determines whether a given input year is a leap
year or no'''
year = int(input("Input: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
