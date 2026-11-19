a = input()

b = 0
c = 0

for i in a:
    if i.isalpha():
        b += 1
    if i.isdigit():
        c += 1

print("Letters", b)
print("Digits", c)