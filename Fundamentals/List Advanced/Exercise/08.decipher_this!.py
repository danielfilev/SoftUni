message = input().split(' ')
char = ''

for i in range(len(message)):
    word = message[i]
    result = word.translate({ord(x): None for x in '0123456789'})

    for letter in range(len(word)):
        if word[letter].isdigit():
            char += word[letter]
    word = chr(int(char))

    if len(result) > 1:
        print(word + result[-1:] + result[1:-1] + result[:1], end=' ')
    elif len(result) == 1:
        print(word + result, end=' ')
    char = ''
