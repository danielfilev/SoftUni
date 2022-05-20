str = input()
ll = [i for i in str]
s = []

for i in range(len(str)):
    if str[i] == "(":
        s.append(i)
    elif str[i] == ")":
        opened_bracket = s.pop()
        closed_bracket = i
        print("".join(ll[opened_bracket:closed_bracket+1]))
