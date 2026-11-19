d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answers = []

for i in range(3):
    a = input()
    n, m = map(int, input().split())

    x = int(a, n)
    b = ""
    z = abs(x)

    while z > 0:
        b = d[z % m] + b
        z = z // m

    if x == 0:
        b = "0"
    if x < 0:
        b = "-" + b

    answers.append(b)

for b in answers:
    print(b)