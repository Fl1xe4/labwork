a = input().split(",")

for i in range(len(a)):
    a[i] = a[i].strip()

a.sort(key=str.lower, reverse=True)

print(*a)