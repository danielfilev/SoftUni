vowels = ["a", "o", "u", "i", "e"]
string = input()
no_vowels = [i for i in string if i not in vowels]
print("".join(no_vowels))
