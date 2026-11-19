a = input()
b = input()
c = input()

for x in (a, b, c):
    if '0' <= x <= '9':
        print("Yes")
    else:
        print("No")