def check_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

print(check_grade(92))
print(check_grade(76))
print(check_grade(60))
print(check_grade(40))
