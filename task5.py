def proddigits(n):
    prod = 1
    while n > 0:
        digit = n % 10
        if digit != 0:
            prod *= digit
        n //= 10
    return prod

n = 74632506475
result = proddigits(n)
print(result)
