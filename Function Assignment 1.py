'''(1)
def outer():
    def inner():
        return "Hello, I'm the inner function!"
    return inner()

ans = outer()
print(ans)

(2)
def outer():
    def inner():
        return "Hello, I'm the inner function!"
    return inner

retObj = outer()
retInner = retObj()
print(retInner)

(3) WAP for function returns the array of factorial of the element
● Pass the array to the function
def factorial_array(arr):
    fact_arr = []
    for num in arr:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        fact_arr.append(fact)
    return fact_arr

input_arr = [1, 2, 3, 4, 5]
output_arr = factorial_array(input_arr)
print(output_arr)  # Output: [1, 2, 6, 24, 120]

(4) WAP for a function that returns the count of the search element in the list

Input:
listData = [1, 2, 3, 3, 4, 5, 3]
serchEle = 3

def count_element(lst, search_ele):
    count = 0
    for ele in lst:
        if ele == search_ele:
            count += 1
    return count

list_data = [1, 2, 3, 3, 4, 5, 3]
search_ele = 3
count = count_element(list_data, search_ele)
print(f"{search_ele} found in list {count} times")  # Output: 3 found in list 3 times

(5) Write the parent function that includes the nested functions digitCount,
evenDigitCount, and oddDigitCount. provide a number to th functions Then, call
all functions and fill in the return value in the list.
def parent_function(num):
    def digit_count(num):
        return len(str(num))
    
    def even_digit_count(num):
        return len([d for d in str(num) if int(d) % 2 == 0])
    
    def odd_digit_count(num):
        return len([d for d in str(num) if int(d) % 2 != 0])

    return [digit_count(num), even_digit_count(num), odd_digit_count(num)]

num = 12345
output = parent_function(num)
print(output)  # Output: [5, 2, 3]

(6) Python program that defines a parent function with two nested functions
(myIndex and myPalindrome). The program prompts the user to choose between
these two functions and then calls the selected function based on the user's
def parent_function(choice, list_data=None, search_ele=None):
    def my_index(choice, list_data, search_ele):
        return list_data.index(search_ele)
    
    def my_palindrome(choice, num):
        return str(num) == str(num)[::-1]
    
    if choice == 1:
        return my_index(choice, list_data, search_ele)
    elif choice == 2:
        return my_palindrome(choice, num)

choice = 1
list_data = [1, 2, 3, 4, 5, 6]
search_ele = 2
print(parent_function(choice, list_data, search_ele))  # Output: 1

choice = 2
num = 141
print(parent_function(choice, num))  # Output: True

(7) WAP defines a class Sum with a mySum method that returns the sum of two numbers.
The program creates two class objects, takes user input to set values for each object,
prints the return sum for both objects, and then determines whether the total sum is even
or odd.
class Sum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def mySum(self):
        return self.num1 + self.num2

num1_1 = int(input("Object1 input:\nNum1 = "))
num2_1 = int(input("Num2 = "))
object1 = Sum(num1_1, num2_1)

num1_2 = int(input("Object input:\nNum1 = "))
num2_2 = int(input("Num2 = "))
object2 = Sum(num1_2, num2_2)

sum1 = object1.mySum()
sum2 = object2.mySum()

total_sum = sum1 + sum2
if total_sum % 2 == 0:
    print(f"Sum is Even {total_sum}")
else:
    print(f"Sum is Odd {total_sum}")

(8) Write a realtime example of oop which contains the following point.
a. Instance variable
b. constructor
c. Class variable
d. Instance method

class Employee:
    company = "XYZ Corp"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age
    
    def display_info(self):  # Instance method
        print(f"Name: {self.name}, Age: {self.age}")

emp1 = Employee("John", 30)
emp2 = Employee("Alice", 25)

emp1.display_info()  # Output: Name: John, Age: 30
emp2.display_info()  # Output: Name: Alice, Age: 25

(9) 9. Write a real-time example of OOP on IPL cricket by the following point.
a. Instance variable
b. constructor
c. Class variable
d. Instance method

class Player:
    team = "RCB"  # Class variable

    def __init__(self, name, jersey_number):
        self.name = name  # Instance variable
        self.jersey_number = jersey_number
    
    def display_info(self):  # Instance method
        print(f"Name: {self.name}, Jersey Number: {self.j

 (10) Write a program in which you have to write a __new__ user-defined function that
creates a new instance of a class.    
class MyClass:
    def __new__(cls, *args, **kwargs):
        # Create a new instance of the class
        instance = super().__new__(cls)
        print("New instance created")
        return instance

    def __init__(self, value):
        self.value = value

# Create a new instance of MyClass
obj = MyClass(10)
print("Value of the instance:", obj.value)'''
