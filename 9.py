n = int(input('Сколько точек может быть на одной плитке? '))
total = 0

for i in range(0, n + 1):
    for j in range(0, i + 1):
        total += (i + j)

print(total)