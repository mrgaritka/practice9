n = int(input())
count = 0

while n != 0:
    n = int(input())
    if n % 4 == 0 and n != 0:
        count += 1
    if n == 0:
        break

print(count)