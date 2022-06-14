def negative_vs_positive(*args):
    positives = []
    negatives = []
    for number in args:
        if number > 0:
            positives.append(number)
            continue
        negatives.append(number)

    print(f"{sum(negatives)}")
    print(f"{sum(positives)}")
    if abs(sum(negatives)) > abs(sum(positives)):
        return f"The negatives are stronger than the positives"
    else:
        return f"The positives are stronger than the negatives"


data = [int(x) for x in input().split()]
print(negative_vs_positive(*data))
