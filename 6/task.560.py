a = input().lower()

abc = "abcdefghijklmnopqrstuvwxyz"
b = {}

for letter in abc:
    b[letter] = 0

for letter in a:
    if letter in b:
        b[letter] += 1

print(*b.values())
