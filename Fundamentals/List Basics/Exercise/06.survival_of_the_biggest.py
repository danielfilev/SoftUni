string1 = input().split(' ')
list1 = list(map(int, string1))
n = int(input())

for instances in range(n):
    smallest_element = min(list1)
    string1.remove(str(smallest_element))
    list1.remove(smallest_element)

print(', '.join(string1))
