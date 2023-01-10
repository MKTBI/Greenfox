'''Sort matrix
Create a function called sort_matrix that takes a multidimensional array which represents a square matrix, as a parameter, and returns a same n x n sized matrix in which the elements are sorted in ascending order. (for sorting you can use the built in sort or sorted list method)

Example
Input
[
  [4, 2, 3],
  [2, 1, 7],
  [7, 2, 6]
]
Output
[
  [1, 2, 2],
  [2, 3, 4],
  [6, 7, 7]
]

Example 2
Input
[
  [8, 5],
  [2, 7]
]
Output
[
  [2, 5],
  [7, 8]
]
Handle edge cases, invalid input and the like, and argue for and against your choices.'''

def sort_matrix(matrix):
    try:
        flat_matrix = [x for sublist in matrix for x in sublist]
        flat_matrix.sort()

        
        n = len(matrix)
        new_matrix = [[0 for _ in range(n)] for _ in range(n)]
        idx = 0
        for i in range(n):
            for j in range(n):
                new_matrix[i][j] = flat_matrix[idx]
                idx += 1

        return new_matrix
    except:
        print("Invalid input")
        return None

print(sort_matrix(
[
  [8, 5],
  [2, 7]
]))

print(sort_matrix([
  [4, 2, 3],
  [2, 1, 7],
  [7, 2, 6]
]))