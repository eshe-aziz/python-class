def add(x, y):
    result = x + y
    return result

#OUTPUT
#>>> from calculator import add
#>>> answer = add(1000, 2000)
#>>> print(answer)
#3000

#>>> add(1.2, 1.34)
#2.54
#>>> add(10000, 50000)
#60000

def subtract(a, b):
    result = a - b
    return result

#>>> from calculator import subtract
#>>> subtract(20, 30)
#-10

def divide(x1, x2):
    result = x1/x2
    return result

#>>> from calculator import divide
#>>> divide(30, 5)
#6.0

def multiply(e, f):
    result = e * f
    return result

#>>> from calculator import multiply
#>>> multiply(20, 30)
#600

def remainder(g, h):
    result = g % h
    return result

#>>> from calculator import remainder
#>>> remainder(10, 3)
#1


def power(i, j):
    result = i ** j
    return result

#>>> from calculator import power
#>>> power(20, 3)
#8000


# Create a function that can add any amount of numbers:

def sum(*numbers):
    total = 0
    for number in numbers:
        total += number #total = total + number

    return total

# OUTPUT

# >>> from calculator import sum
# >>> sum(10, 20, 30, 40, 50, 60)
# 210


def multiply_many(*numbers):
    total = 1
    for number in numbers:
        total *= number
    
    return total

# OUTPUT: positional arguments

# >>> from calculator import multiply_many
# >>> multiply_many(1, 2, 3, 4)
# 24



# A function that receives a number of keyword arguments and uses the value to create a sentence:
def create_sentence(**words):
    print(words)
    sentence = " "
    for word in words.values():
        sentence += word
        sentence += " "
    
    return sentence

# OUTPUT

# >>> create_sentence(a = "I", b = "love", c = "AkiraChix")
# {'a': 'I', 'b': 'love', 'c': 'AkiraChix'}
# ' IloveAkiraChix'


# A function that accepts any number of positional arguments and keyword arguments:
def sum_and_greet(*args, **kwargs):
    total = 0
    for x in args:
        total += x

    f = kwargs["first_name"]
    l = kwargs["last_name"]

    greeting = f"Hello {f} {l}, the sum of your numbers is {total}"

    return greeting

#OUTPUT

# >>> from calculator import sum_and_greet
# >>> sum_and_greet(10, 20, 30, first_name = "Mutesi", last_name = "Aline")
# 'Hello Mutesi Aline, the sum of your numbers is 60'



















