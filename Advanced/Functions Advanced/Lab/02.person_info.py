def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old."


info1 = {
    'name': 'George',
    'town': 'Sofia',
    'age': 23
}


print(get_info(**info1))
