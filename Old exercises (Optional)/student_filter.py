
students = [
        {'name': 'Mark', 'age': 9.5, 'candies': 2},
        {'name': 'Sean', 'age': 10, 'candies': 1},
        {'name': 'Clark', 'age': 7, 'candies': 3},
        {'name': 'Paul', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def printCandies(students):
    names = [student['name'] for student in students if student['candies'] > 4]
    print("Students with more than 4 candies:", names)

def averageCandies(students):
    candies = [student['candies'] for student in students]
    avg = sum(candies) / len(candies)    
    print("Average number of candies:", avg)


printCandies(students)  # Students with more than 4 candies: ['Paul']
averageCandies(students)  # Average number of candies: 2.75
