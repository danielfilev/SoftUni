word = input()
reverse_word = ""
for syllable in range(len(word) - 1, -1, -1):
    reverse_word += word[syllable]
print(reverse_word)
