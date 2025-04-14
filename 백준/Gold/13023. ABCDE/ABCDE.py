import sys
sys.setrecursionlimit(10000)
# from collections import deque
input = sys.stdin.readline
def dfs(v,node):
    global friend
    if v==5:
        friend=True
        return
    if v>5:
        return
    else:
        for i in board[node]:
            if ch[i]==0 :
                ch[i]=1
                dfs(v+1,i)
                ch[i]=0
n,m=map(int,input().split())
board = [[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    board[a].append(b)
    board[b].append(a)
friend=False
for i in range(n):
    ch=[0]*n
    ch[i]=1
    dfs(1,i)
    if friend==True:
        break
if friend==True:
    print(1)
else:
    print(0)