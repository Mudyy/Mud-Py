def count_vowels(text):
    vowels_found = 0
    for x in text:
        if x == ("a"):
           vowels_found +=1
        elif (x) == ("e"):
            vowels_found +=1
        elif (x) == ("i"):
            vowels_found +=1
        elif (x) == ("o"):
            vowels_found +=1
        elif (x) == ("u"):
            vowels_found +=1
    return vowels_found
print(count_vowels("hello"))
print(count_vowels("rhythm"))
print(count_vowels("education")) 
