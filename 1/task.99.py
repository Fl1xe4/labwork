k = int(input("Введіть кількість рядків на сторінці"))
n = int(input("Введіть номер рядка який потрібно знайти"))

page = (n - 1) // k + 1
position = (n - 1) % k + 1

print(page, position)