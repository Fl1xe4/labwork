n = int(input())

a = []
x = 1

while len(a) < n:
    for i in range(x):
        if len(a) < n:
            a.append(x)
    x += 1

print(*a)