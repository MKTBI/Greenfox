'''Place a knight on an empty chessboard. It has to travel the whole board by visiting each square exactly once. Find a working solution and display it by putting the move numbers into the respective squares.


A solution:

0 59 38 33 30 17 8 63

37 34 31 60 9 62 29 16

58 1 36 39 32 27 18 7

35 48 41 26 61 10 15 28

42 57 2 49 40 23 6 19

47 50 45 54 25 20 11 14

56 43 52 3 22 13 24 5

51 46 55 44 53 4 21 12

https://en.wikipedia.org/wiki/Knight%27s_tour'''


def knights_tour(n: int):
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n

    def dfs(x, y, move_count, chessboard):
        chessboard[x][y] = move_count
        if move_count == n * n:
            return True
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if is_valid(new_x, new_y) and chessboard[new_x][new_y] == -1:
                if dfs(new_x, new_y, move_count + 1, chessboard):
                    return True
        chessboard[x][y] = -1
        return False

    chessboard = [[-1] * n for _ in range(n)]
    dfs(0, 0, 1, chessboard)
    return chessboard

print(knights_tour(3))