# Code 1:
def add(x):
    def inner(y):
        return x * y
    return inner

if __name__== '__main__':
    add_3 = add(3)
    result = add_3(7)
    print(result)  # Output: 21

# Code 2:
def outer():
    def inner():
        return "Greetings from the inner function!"
    return inner()

if __name__== "__main__":
    result = outer()
    print(result)  # Output: "Greetings from the inner function!"

# Code 3:
def outer():
    def inner():
        return "This is the inner function."
    return inner

if __name__== "__main__":
    retObj = outer()
    retInner = retObj()
    print(retInner)  # Output: "This is the inner function."

# Code 4:
def outer():
    def inner():
        return outer
    return inner

if __name__== "__main__":
    retObj = outer()
    retInner = retObj()
    print(retInner)  # Output: "<function outer at 0x000001D3197D20D0>"

# Code 5:
def outer():
    def inner(outer):
        print(outer)
    return inner

if __name__== "__main__":
    retObj = outer()
    print(retObj)  # Output: "<function outer.<locals>.inner at 0x00000208CB5F5DC0>"

# Code 6:
def outer():
    def inner1(a, b):
        print("In inner1")
        return a - b

    def inner2(obj):
        print("In inner2")
        print(obj)
        return inner2

    retInner1 = inner1(10, 4)
    retInner2 = inner2(retInner1)
    return retInner2

if __name__== "__main__":
    retObj = outer()
    print(retObj)  # Output: "<function outer.<locals>.inner2 at 0x00000208CB5F5DC0>"

# Code 7:
def outer():
    def inner():
        return "Hello, Core2web!"
    print("In Outer Function")
    return inner

if __name__== "__main__":
    result = outer()()
    print(result)  # Output: "Hello, Core2web!"

# Code 8:
def outer():
    message = "I am the outer function."
    def inner():
        return message
    return inner

if __name__== "__main__":
    inner_function = outer()
    result = inner_function()
    print(result)  # Output: "I am the outer function."

# Code 9:
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

if __name__== "__main__":
    counter = outer()
    print(counter())  # Output: 1
    print(counter())  # Output: 2

# Code 10:
def outer(flag):
    def inner():
        return "This is true." if flag else "This is false."
    return inner

if __name__== "__main__":
    true_function = outer(True)
    false_function = outer(False)
    print(true_function())  # Output: "This is true."
    print(false_function())  # Output: "This is false."
