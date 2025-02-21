# Lesson 21

upper_limit = int(input())

max_count = 0
result_num = 0

for num in range(1, upper_limit+1):
    total_factors = 0

    for divider in range(1, num+1):
        if num % divider == 0:
            total_factors += 1

        if total_factors > max_count:
            max_count = total_factors
            result_num = num

print(f"{result_num} had the most factors, with {max_count} factors.")
