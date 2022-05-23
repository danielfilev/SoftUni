stack = []
str = input()

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
}

balanced = True
for i in str:
    if i in "([{":
        stack.append(i)
    elif not stack:
        balanced = False
    else:
        last_open_bracket = stack.pop()
        if pairs[last_open_bracket] != i:
            balanced = False

    if not balanced:
        break

if not balanced or stack:
    print("NO")
else:
    print("YES")
