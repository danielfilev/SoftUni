n = int(input())
p = int(input())

courses = n // p
bonus_courses = 0

if courses == 0:
    courses += 1
    print(courses)
elif n - (courses * p) >= 0:
    people_left = n % p
    if people_left > 0:
        bonus_courses += 1
        print(courses + bonus_courses)
    else:
        print(courses)
