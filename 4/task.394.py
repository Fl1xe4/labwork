a = input()
abc = "abcdefghijklmnopqrstuvwxyz"

k = 0
b = 0

for i in a:
    if i.lower() in abc:
        b += 1
        if b > k:
            k = b
    else:
        b = 0

result = ""

for i in a:
    if i.lower() in abc:
        n = abc.index(i.lower())
        x = abc[(n + k) % 26]

        if i.isupper():
            x = x.upper()

        result += x
    else:
        result += i

print(result)