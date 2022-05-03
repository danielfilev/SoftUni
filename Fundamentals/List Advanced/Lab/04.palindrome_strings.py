words = input().split(" ")
special_palindrome = input()
palindromes = list()

for word in words:
    rev_list = reversed(word)
    rev_word = "".join(rev_list)
    if rev_word == word:
        palindromes.append(word)


print(palindromes)
palindrome_count = words.count(special_palindrome)
print(f"Found palindrome {palindrome_count} times")
