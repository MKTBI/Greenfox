#num = int(input("write your number here: "))
def summing(x):
    sum = 0
    for i in range(num):
        sum += i + 1
    print(sum)
#summing(num)

def summing2(x):
    sum_of_numbers = 0
    for i in range(1, x + 1):
        sum_of_numbers += i
        #print(sum_of_numbers)

    return sum_of_numbers

my_sum = summing2(5)
print(my_sum)
