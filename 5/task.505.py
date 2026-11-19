a = []

for row in input().split(","):
    a.append(list(map(int, row.split())))

n = len(a)
s = sum(a[0])
result = True

x = 0
y = 0

for i in range(n):
    if sum(a[i]) != s:
        result = False

    t = 0
    for j in range(n):
        t += a[j][i]

    if t != s:
        result = False

    x += a[i][i]
    y += a[i][n - 1 - i]

if x != s or y != s:
    result = False

print(result)