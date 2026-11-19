a, b = map(int, input().split())

c = []

for i in range(a):
    row = []
    for j in range(b):
        row.append(i * j)
    c.append(row)

print(c)