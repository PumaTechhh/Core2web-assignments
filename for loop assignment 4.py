# Program 1: Print numbers from a given range
start = 100
end = 110
for num in range(start, end + 1):
    print(num, end=" ")
print("\n")

# Program 2: Print all even numbers from a given range
start = 10
end = 20
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")
print("\n")

# Program 3: Print sum of all numbers from a given range
start = 1
end = 10
total = 0
for num in range(start, end + 1):
    total += num
print("Sum:", total)
print("\n")

# Program 4: Print character values of given ASCII value range
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
if start > end:
    print("Wrong input")
else:
    for ascii_val in range(start, end + 1):
        print(f"The character of ASCII value {ascii_val} is {chr(ascii_val)}")
print("\n")

# Program 5: Print numbers divisible by 7 but not by 3 in a given range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
for num in range(start, end + 1):
    if num % 7 == 0 and num % 3 != 0:
        print(num, end=" ")
print("\n")

# Program 6: Print ASCII values from a given character range
start = input("Enter the start of range: ")
end = input("Enter end of range: ")
for char in range(ord(start), ord(end) + 1):
    print(f"ASCII value of {chr(char)} is {char}")
print("\n")

# Program 7: Print all positive numbers from a given range
start = -7
end = 8
for num in range(start, end + 1):
    if num > 0:
        print(num, end=" ")
print("\n")

# Program 8: Print numbers divisible by 3 and 5 both in a given range
start = 15
end = 50
for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=" ")
print("\n")

# Program 9: Print count of all negative numbers from a given range
start = -15
end = 50
count = 0
for num in range(start, end + 1):
    if num < 0:
        count += 1
print(count)
print("\n")

# Program 10: Print product of count of odd numbers within a given range
start = 1
end = 11
count = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        count += 1
product = 1
for i in range(count):
    product *= count
print(product)
