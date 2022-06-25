def shopping_cart(*args):
    result = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }

    ll = []
    for item in args:
        ll.append(item)

    for el in ll:
        if el == "Stop":
            break
        elif el[0] == 'Soup' and len(result['Soup']) < 3:
            if el[1] not in result['Soup']:
                result['Soup'].append(el[1])
        elif el[0] == 'Pizza' and len(result['Pizza']) < 4:
            if el[1] not in result['Pizza']:
                result['Pizza'].append(el[1])
        elif el[0] == 'Dessert' and len(result['Dessert']) < 2:
            if el[1] not in result['Dessert']:
                result['Dessert'].append(el[1])

    sorted_result = dict(sorted(
        result.items(), key=lambda x: (-len(x[1]), x[0], x[1].sort())))

    x = ''
    for key, item in sorted_result.items():
        x += f"{key}:\n"
        for el in item:
            x += f" - {el}\n"

    if len(sorted_result['Soup']) > 0 or len(sorted_result['Pizza']) > 0 or len(sorted_result['Dessert']) > 0:
        return x
    return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
