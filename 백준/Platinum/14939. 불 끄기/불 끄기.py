import sys
input = sys.stdin.readline

dy = [0, 0, 1, 0, -1]
dx = [0, 1, 0, -1, 0]

def press(b, y, x):
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < 10 and 0 <= nx < 10:
            b[ny][nx] = (b[ny][nx] + 1) % 2

def generate_combinations():
    from itertools import product
    return list(product([0, 1], repeat=10))

def solve():
    board = [[1 if x == 'O' else 0 for x in input().strip()] for _ in range(10)]
    best = float('inf')
    combinations = generate_combinations()

    for first_row in combinations:
        temp_board = [row[:] for row in board]
        presses = 0

        # 첫 번째 행 처리
        for col in range(10):
            if first_row[col] == 1:
                press(temp_board, 0, col)
                presses += 1

        # 나머지 행 처리
        for row in range(1, 10):
            for col in range(10):
                if temp_board[row - 1][col] == 1:
                    press(temp_board, row, col)
                    presses += 1

        # 마지막 행 검사
        if all(temp_board[9][col] == 0 for col in range(10)):
            best = min(best, presses)

    return -1 if best == float('inf') else best

print(solve())
