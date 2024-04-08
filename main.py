"""
OrderOfNumbers
"""
# Provide your solution here
n1 = int(input("n1: "))
n2 = int(input("n2: "))

if n1 <= 0 and n2 <= 0:
    print("n1 and n2 need to be > 0")
elif n1 < n2:
    print(n1, n2)
elif n1 > n2:
    print("n2 need to be > n1")


"""
SumUp
"""
# Provide your solution here
n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

if n1 > n2 and n2 > n3 and n1 > n3:
    print("numbers are descending")
elif n3 > n2 and n2 > n1 and n3 > n1:
    print("numbers are ascending")
elif n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
    print("no specific order, but all even")
elif n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
    print("no specific order, but all odd")
else:
    print("no specific order")