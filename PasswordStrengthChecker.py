def check_password(pwd):
    if len(pwd) >= 8:
       return "Strong password"
    else:
        return "weak password"

print(check_password("hello"))
print(check_password("supersecure123"))
