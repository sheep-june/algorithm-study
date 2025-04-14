import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m,n=map(int,input().split())
board = []
q = deque()
for i in range(n):
    tomato=list(map(int,input().split()))
    board.append(tomato)
    for j in range(m):
        if tomato[j] == 1:
            q.append((i, j))
cnt=0
while q:
    cnt += 1
    for _ in range(len(q)):
        xx, yy = q.popleft()
        for k in range(4):
            x = xx + dx[k]
            y = yy + dy[k]
            if 0<=x<n and 0<=y<m and board[x][y]==0:
                board[x][y]=1
                q.append((x,y))
for row in board:
    if 0 in row:
        print(-1)
        sys.exit()
print(cnt-1 if cnt>1 else 0)