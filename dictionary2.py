"""

#create

student = {"name": "Ali", "age":20}

#add new key-value
student["grade"] = "A"

#update
student["age"] = 21

#Delete
del student["grade"]

#check existence
print("age" in student)

print(student.get("grade","Not found"))

"""
"""
student = {"name": "Ali", "age":20, "grade":"A"}

#keys
for key in student:
    print(key)

for value in student.values():
    print(value)

for key,value in student.items():
    print(key,":",value)
"""

shopping_cart = {"Apples":100,"Butter":250,"Eggs":200}
for item,price in shopping_cart.items():
    print(item,":",price)
