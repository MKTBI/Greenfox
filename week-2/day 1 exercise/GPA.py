lst = []
marks = input("please write 5 numbers separated by space: ")
marks_split = marks.split(" ")
total_sum = 0
lst.append(marks)
for lst in range(marks):
    marks_split = float(input('Enter number : '))
    total_sum += marks
avg = total_sum / marks
print('Average of ', marks, ' numbers is :', avg)
print(total_sum)