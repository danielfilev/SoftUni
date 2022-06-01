text = input()
dic = {}


for ch in text:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1

for key, value in sorted(dic.items()):
    print(f"{key}: {value} time/s")
