# Program 1: Print the First 10 Numbers
print("Program 1: Print the First 10 Numbers")
for i in range(1, 11):
    print(i)

# Program 2: Print the First 100 Numbers
print("\nProgram 2: Print the First 100 Numbers")
for i in range(1, 101):
    print(i)

# Program 3: Print the First Ten 3-Digit Numbers
print("\nProgram 3: Print the First Ten 3-Digit Numbers")
for i in range(100, 111):
    print(i)

# Program 4: Print Even Numbers from 1 to 100
print("\nProgram 4: Print Even Numbers from 1 to 100")
for i in range(2, 101, 2):
    print(i)

# Program 5: Print Odd Numbers from 1 to 50
print("\nProgram 5: Print Odd Numbers from 1 to 50")
for i in range(1, 51, 2):
    print(i)

# Program 6: Print Numbers in Reverse from 100 to 1
print("\nProgram 6: Print Numbers in Reverse from 100 to 1")
for i in range(100, 0, -1):
    print(i)

# Program 7: Print Table of 12
print("\nProgram 7: Print Table of 12")
for i in range(1, 11):
    print(f"12 * {i} = {12 * i}")

# Program 8: Print Table of 12 in Reverse Order
print("\nProgram 8: Print Table of 12 in Reverse Order")
for i in range(10, 0, -1):
    print(f"12 * {i} = {12 * i}")

# Program 9: Print Sum of the First 10 Numbers
print("\nProgram 9: Print Sum of the First 10 Numbers")
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

# Program 10: Print Product of the First 10 Numbers
print("\nProgram 10: Print Product of the First 10 Numbers")
product = 1
for i in range(1, 11):
    product *= i
print("Product:", product)
