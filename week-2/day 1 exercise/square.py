a = eval(input("Please enter a number :"))
for x in range(1):
    print("%" * a)
for x in range(1,a-1):
    print("%"," " * (a-4),"%")
for x in range(a - 1 , a):
    print("%" * a)
