def perfect(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n

def perfect_numbers_up_to(x):
    perfect_numbers = []
    for i in range(1, x + 1):
        if perfect(i):
            perfect_numbers.append(i)
    return perfect_numbers

x = 10000
perfect_numbers = perfect_numbers_up_to(x)
print(f"Совершенные числа, не превосходящие {x}: {perfect_numbers}")

