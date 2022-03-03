a = int(input("three-digit number "))
b = int(input("two-digit number "))
a1 = a % 10
b1 = b % 10
a2 = (a % 100) // 10
b2 = b // 10
a3 = a // 100
t1 = (a1 + b1) % 10
t2 = (a2 + b2 + (a1 + b1) // 10) % 10
t3 = a3 + ((a2 + b2 + (a1 + b1) // 10) // 10)
print("number of hundreds", t3)
print("number of tens", t2)
print("number of units", t1)