# import math
import sys
# sys.setrecursionlimit(10**4)
from collections import deque
# from queue import PriorityQueue
input = sys.stdin.readline
se=[0,0,1,1,2,2]
re=[1,2,0,2,0,1]
now=list(map(int,input().split()))
visited=[[False for j in range(201)]for i in range(201)]
answer=[False]*201
def bfs():
    q=deque()
    q.append((0,0))
    visited[0][0]=True
    answer[now[2]]=True
    while q:
        nNode=q.popleft()
        a=nNode[0]
        b=nNode[1]
        c=now[2]-a-b
        for k in range(6):
            next=[a,b,c]
            next[re[k]] += next[se[k]]
            next[se[k]]=0
            if next[re[k]]>now[re[k]]:
                next[se[k]]=next[re[k]]-now[re[k]]
                next[re[k]]=now[re[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]]=True
                q.append((next[0],next[1]))
                if next[0]==0:
                    answer[next[2]]=True
bfs()
for i in range(len(answer)):
    if answer[i]:
        print(i,end=' ')