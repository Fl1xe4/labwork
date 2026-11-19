a = input()

x = "abcdefgh".index(a[0])
y = int(a[1]) - 1

for i in range(7, -1, -1):
    for j in range(8):
        if j == x and i == y:
            print("B", end=" ")
        elif abs(j - x) == abs(i - y):
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()