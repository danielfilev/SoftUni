string = list(map(int, input().split(", ")))

positive = [x for x in string if x >= 0]
negative = [x for x in string if x < 0]
even = [x for x in string if x % 2 == 0]
odd = [x for x in string if x % 2 != 0]

positive = ", ".join(list(map(str, positive)))
negative = ", ".join(list(map(str, negative)))
even = ", ".join(list(map(str, even)))
odd = ", ".join(list(map(str, odd)))

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
