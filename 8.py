x = int(input())
ap = []

for i in range(1,x+1):
    for j in range(1,x+1):
        if i**2 + j**2 == x:
            ap.append(i)
            ap.append(j)

print(int(len(set(ap)) / 2))