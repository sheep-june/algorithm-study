import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]  
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, input().split())  
board = []
q = deque()

for z in range(h):  
    layer = []
    for i in range(n):
        row = list(map(int, input().split()))
        layer.append(row)
        for j in range(m):
            if row[j] == 1:
                q.append((z, i, j))
    board.append(layer)

cnt = 0

while q:
    for _ in range(len(q)):
        zz, xx, yy = q.popleft()
        for k in range(6):  
            z = zz + dz[k]
            x = xx + dx[k]
            y = yy + dy[k]
            if 0 <= z < h and 0 <= x < n and 0 <= y < m and board[z][x][y] == 0:
                board[z][x][y] = 1
                q.append((z, x, y))
    cnt += 1

for layer in board: 
    for row in layer:
        if 0 in row:
            print(-1)
            sys.exit()

print(cnt - 1 if cnt > 1 else 0)