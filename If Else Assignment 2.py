'''WAP to check numbers are divisible by 4 and 5
Print those numbers
Input1: num1 =20
Output:
20 is divisible by 4 and 5
Input1: num1 =15
Output:
15 is not divisible by 4 and 5'''

num1 = int(input("Input: "))

if num1 % 4 == 0 and num1 % 5 == 0:
    print(num1, "is divisible by 4 and 5")
else:
    print(num1, "is not divisible by 4 and 5")

'''WAP to determine whether entered angles define a right-angled triangle.
Take three values of angle from the user.
Input1: angel1 = 90
Input2: angle2 = 90
Input3: angle3 = 90
Output:
It is not a right-angle triangle
Input1: angel1 = 90
Input2: angle2 = 60
Input3: angle3 = 30
Output:
It is a right-angle triangle'''

angle1 = int(input("Input1: "))
angle2 = int(input("Input2: "))
angle3 = int(input("Input3: "))

if angle1 + angle2 + angle3 == 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("It is a right-angle triangle")
    else:
        print("It is not a right-angle triangle")
else:
    print("Invalid input: The angles do not sum up to 180 degrees")

'''Take two numbers from users and print the sum of those numbers
if the sum is even.
Input1: num1 = 10
Input2: num2 = 20
Output: 30 is Even
Input1: num1 = 10
Input2: num2 = 15
Output: No Output'''

num1 = int(input("Input1: "))
num2 = int(input("Input2: "))
sum_nums = num1 + num2

if sum_nums % 2 == 0:
    print(sum_nums," is Even")
else:
    print(sum_nums," is Odd")

'''Take a number from the user and check whether it is present in the list. If
it's in the list, print "Available."
List1 = [10, 20, 30, 40, 50]
#input: num = 10
#Output: available
#input num = 15
#Output:No Output'''
List1 = [10, 20, 30, 40, 50]
num = int(input("Input num: "))
if num in List1:
    print("Available")

'''Print the "Core2web" string a number of times entered by the user if the
number is even.
#Input: num = 2
#Output: Core2web
Core2web
#Input: num = 5
#Output: No Output'''

num = int(input("Input: "))
if num % 2 == 0:
    for _ in range(num):
        print("Core2web")

'''Write a program that checks if a given number is odd using the "if"
statement.
#Input num = 13
#Output: Odd
#Input: num = 12
#Output: No Output'''

num = int(input("Input: "))
if num % 2 != 0:
    print("Odd")
else:
    print("no output")

'''Take two numbers from the user, check if both are odd and then print the
sum of the numbers.
#Input: num1 = 10
#Input: num2 = 11
#Output: 21
#Input: num1 = 10
#Input: num2 = 6
#Output: No Output'''

num1 = int(input("Input: num1 = "))
num2 = int(input("Input: num2 = "))
if num1 % 2 != 0 and num2 % 2 != 0:
    print(num1 + num2)
else:
    print("No Output")

'''Take single character from user check if the ascii value of character is
Even the print character.
#Input char1 = ‘B’
#Output: B
#Input char1 = ‘C’
#Output: No Output'''

char1 = input("Input: ")
if ord(char1) % 2 == 0:
    print(char1)
else:
    print("No Output")

'''Take Two character from user check if the ascii value both of character are
odd then print the sum of ascii values of character
#Input: char1 = ‘A’
char2 = ‘C’
#Output: 132
#Input: char1 = ‘a’
char2 = ‘b’
#Output:No Output"'''

char1 = input("Input: char1 = ")
char2 = input("Input: char2 = ")
if ord(char1) % 2 != 0 and ord(char2) % 2 != 0:
    print(ord(char1) + ord(char2))
else:
    print("No Output")

'''Take the number from user and modulus with 8 if the reminder of the
number is 3 then print reminder.
#Input num = 27
#Output: 3
#Input: num = 10
#Output: No Output'''

num = int(input("Input: "))
if num % 8 == 3:
    print(num % 8)
else:
    print("No Output")
