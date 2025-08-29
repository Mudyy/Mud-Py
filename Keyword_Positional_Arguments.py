def greet(name,age):
    return f"Hello {name}, you are {age} years old."
    
#positional Arguments - Order does matter
print(greet("Ali", 25))

#Keyword Arguments - Order doesn't matter
print(greet(age=25,name="Ali"))

#Keyword Arguments Excercise - Order doesn't matter
def student_info(name,grade,age):
    return f"Hello {name}, from {grade}, you are {age}"
#Keyword Arguments - Order doesn't matter    
print(student_info(name="Ali",grade=7,age=14))
