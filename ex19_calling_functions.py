#variable
# x = 10

#def print_one(arg1):
    #print(f"arg1:{arg1}")

# The parameter arg1 is a variable similar
# to the x before, except its created for
# for you when you call the function like this:

# print_one("First!")

"""In Excercise 18, you learned how python
runs functions when you call them, but what
happens if you did this: """

#y = "First!"
#print_one(y)

"""Instead of calling print_one directly
with First! you're assigning First! to y and then
passing y to print_one. Does this work?
Here's a small sample code you can use to test
this out """

def print_one(args1):
    print(f"arg1:{args1}")

y = "First!"
print_one(y)
