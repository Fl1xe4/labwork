n = int(input())

a = {}

for i in range(n):
    x, y = input().split()
    a[x] = y
    a[y] = x

word = input()

print(a[word])
