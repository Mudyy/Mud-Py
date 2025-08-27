def count_vowels_again(textagain):
    vowel_foundagain = 0
    for ch in (textagain):
        if ch in "aieou":
            vowel_foundagain +=1
    return vowel_foundagain
print(count_vowels_again("Hello"))
print(count_vowels_again("rhythm"))
print(count_vowels_again("education"))
