#Functions
def hello():
    print("Hello AkiraChix")

def hello(name):
    print(f"Hello {name}")


#Keyword arguments- year_of_birth(name= "Raziah", age = 20) prefered if you have so many parameters
def year_of_birth(name, age):
    print(f"Hello {name}, was born in {2024-age}")

def my_country(country = "Uganda"):
    print(f"Hello AkiraChix from {country}")

##Output
#>>> from hello import my_country
#>>> my_country()
#Hello AkiraChix from Uganda
#>>> my_country(country = "Rwanda")
#Hello AkiraChix from Rwanda
#>>> my_country(country = "Kenya")
#Hello AkiraChix from Kenya

###################################################################################################################
# A function that accepts any number of positional arguments

def greet(name):
    print(f"Hello {name}")

# OUTPUT

# >>> from hello import greet
# >>> greet("ALice")
# Hello ALice
# >>> greet("ALice", "Nancy")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: greet() takes 1 positional argument but 2 were given

def greet(*names):
    for name in names:
        print(f"Hello {name}")

# OUTPUT

# >>> from hello import greet
# >>> greet("Alice", "Nancy")
# Hello Alice
# Hello Nancy








