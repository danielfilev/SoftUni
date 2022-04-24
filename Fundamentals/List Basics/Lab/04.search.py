n = int(input())
special_word = input()
list1 = []
list2 = []
for i in range(n):
    new_word = input()
    list1.append(new_word)
    if special_word in new_word:
        list2.append(new_word)
print(list1)
print(list2)
