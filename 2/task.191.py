a = int(input("Введіть висоту цеглини"))
b = int(input("Введіть ширину цеглини"))
c = int(input("Введіть довжину цеглини"))
d = int(input("Введіть висоту отвір"))
e = int(input("Введіть ширину отвір"))

if ((a <= d and b <= e) or (a <= e and b <= d)):
    print("Yes")
else:
    print("No")