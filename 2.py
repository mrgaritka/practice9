num = int(input())

while num**0.5 > 2:
    print(round(num**0.5, 3))
    num = num ** 0.5
    if num**0.5 <= 2:
        print(round(num ** 0.5, 3))
        break