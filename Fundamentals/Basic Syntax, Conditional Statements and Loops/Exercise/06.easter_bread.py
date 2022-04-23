budget = float(input())
price_for_flour_1kg = float(input())
price_for_eggs_1pack = price_for_flour_1kg * 0.75
price_for_milk = (price_for_flour_1kg * 1.25) / 4
total_price_loaf = price_for_flour_1kg + price_for_eggs_1pack + price_for_milk
current_loaf_count = 0
current_egg_count = 0
while budget > total_price_loaf:
    budget -= total_price_loaf
    current_loaf_count += 1
    while current_loaf_count > 0:
        current_egg_count += 3
        if current_loaf_count % 3 == 0:
            current_egg_count -= current_loaf_count - 2
            break
        break
print(f"You made {current_loaf_count} loaves of Easter bread! Now you have {current_egg_count} eggs and {budget:.2f}BGN left.")
