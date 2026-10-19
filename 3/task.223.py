numbers = []

while True:
    n = int(input())

    if n < 10:
        continue

    if n > 100:
        break

    numbers.append(n)

for n in numbers:
    print(n)