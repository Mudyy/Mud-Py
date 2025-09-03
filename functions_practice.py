# functions_practice.py
# Collection of function exercises and experiments (after Ex 19)

# ------------------------------
# Basic functions
# ------------------------------
def do_nothing():
    pass  # placeholder function

def do_something():
    print("I did something")

def do_more_things(a, b):
    print("A IS", a, "B IS", b)

# ------------------------------
# Functions with arguments
# ------------------------------
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1:{arg1}, arg2:{arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():
    print("I got nothin'.")

# ------------------------------
# Variable vs literal arguments
# ------------------------------
def show_arg(arg1):
    print(f"arg1:{arg1}")

# ------------------------------
# Function chaining examples
# ------------------------------
def give_number():
    return 7

def double(n):
    return n * 2

def add_three(n):
    return n + 3

def subtract_five(n):
    return n - 5

def half(n):
    return n / 2

def give_word():
    return "Code"

def repeat_word(word):
    return word * 3

def word_length(word):
    return len(word)

def make_message(num):
    return f"The magic number is {num}"

def square(n):
    return n * n

def cube(n):
    return n ** 3

# ------------------------------
# Demo calls
# ------------------------------
if __name__ == "__main__":
    do_something()
    do_more_things("hello", 1)

    print_two("Zed", "Shaw")
    print_two_again("Zedi", "Shawi")
    print_one("First!")
    print_none()

    y = "First!"
    show_arg(y)

    # Function chaining
    print("Chaining examples:")
    print(add_three(double(give_number())))   # 17
    print(subtract_five(double(give_number())))  # 9
    print(half(subtract_five(double(give_number()))))  # 4.5

    # String and number mix
    print(repeat_word(give_word()))           # CodeCodeCode
    print(word_length(repeat_word(give_word())))  # 12
    print(make_message(square(word_length("Python"))))  # The magic number is 36
    print(make_message(cube(word_length("Hello"))))     # The magic number is 125

    # Combo pipeline
    a = "Coding"
    length = word_length(a)       # 6
    squared = square(length)      # 36
    cubed = cube(squared)         # 46656
    print(make_message(cubed))    # The magic number is 46656
