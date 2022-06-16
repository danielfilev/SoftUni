def palindrome(word, index):
    def is_palindrome(word):
        return word == word[::-1]
    ans = is_palindrome(word)
    if ans:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
