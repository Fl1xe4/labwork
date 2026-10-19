a = int(input())
b = int(input())

for n in [a, b]:
    x = n
    k = 1

    while x > 0:
        k = k * 10
        x = x // 10

    if (n * n) % k == n:
        print(True)
    else:
        print(False)