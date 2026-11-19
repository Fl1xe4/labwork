a = list(map(int, input().split()))

x = a.index(min(a))
y = a.index(max(a))

a[x], a[y] = a[y], a[x]

print(*a)