num1 = int(input())
num2 = int(input())

n1_1 = num1 // 1000
n1_2 = (num1 // 100) % 10
n1_3 = (num1 // 10) % 10
n1_4 = num1 % 10

if (n1_1 != n1_2 and n1_1 != n1_3 and n1_1 != n1_4 and n1_2 != n1_3 and n1_2 != n1_4 and n1_3 != n1_4):
    print(True)
else:
    print(False)

n2_1 = num2 // 1000
n2_2 = (num2 // 100) % 10
n2_3 = (num2 // 10) % 10
n2_4 = num2 % 10

if (n2_1 != n2_2 and n2_1 != n2_3 and n2_1 != n2_4 and n2_2 != n2_3 and n2_2 != n2_4 and n2_3 != n2_4):
    print(True)
else:
    print(False)
