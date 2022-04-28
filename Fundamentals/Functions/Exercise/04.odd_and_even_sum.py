def odd_even_sum(int1, even, odd):
    for digit in range(len(str(int1))):
        last_digit = int1 % 10
        if last_digit % 2 == 0:
            even += last_digit
        else:
            odd += last_digit
        remaining_num = int1 // 10
        int1 = remaining_num
    print(f"Odd sum = {odd}, Even sum = {even}")


positive_sum = 0
negative_sum = 0
num = int(input())
odd_even_sum(num, positive_sum, negative_sum)
