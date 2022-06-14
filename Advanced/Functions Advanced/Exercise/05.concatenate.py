def concatenate(*args, **kwargs):
    mainstring = ''
    for el in args:
        mainstring += el
    for key, value in kwargs.items():
        if key in mainstring:
            mainstring = mainstring.replace(key, value)
    return mainstring


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
