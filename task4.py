def multiplication(n):
    table = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
    return table

n = 9
table = multiplication(n)
#print(multiplication(9))

for row in table:
    print(row)