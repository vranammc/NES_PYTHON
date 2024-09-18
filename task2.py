def main(L, n):
    n = n % len(L)
    return L[-n:] + L[:-n]

print(main([1, 3, 4, 2, 7, 5], 2))  # [7, 5, 1, 3, 4, 2]
print(main([1, 3, 4, 2, 7, 5], -2))  # [4, 2, 7, 5, 1, 3]
print(main ([1, 3, 4, 2,7, 5], 7))