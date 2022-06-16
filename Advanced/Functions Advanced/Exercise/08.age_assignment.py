def age_assignment(*args, **kwargs):
    results = []
    for key in kwargs:
        for name in args:
            if name[0] == key:
                results.append(f"{name} is {kwargs[key]} years old.")
    return "\n".join(sorted(results))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
