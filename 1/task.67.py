a = int(input("Введіть гривні"))
b = int(input("Введіть копійки"))
n = int(input("Введіть кількість книг"))

total_kopecks = (a * 100 + b) * n

hryvnias = total_kopecks // 100
kopecks = total_kopecks % 100

print(hryvnias, kopecks)