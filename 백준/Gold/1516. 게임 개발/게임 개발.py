# import math
import sys

# sys.setrecursionlimit(10 ** 5)
from collections import deque
# from queue import PriorityQueue
input = sys.stdin.readline
n=int(input())
a=[[]for _ in range(n+1)]
indegree=[0]*(n+1)
selfBuild=[0]*(n+1)
for i in range(1,n+1):
    inputList=list(map(int,input().split()))
    selfBuild[i]=inputList[0]
    index=1
    while True:
        preTemp=inputList[index]
        index += 1
        if preTemp==-1:
            break
        a[preTemp].append(i)
        indegree[i] += 1
q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)
res=[0]*(n+1)
while q:
    now=q.popleft()
    for next in a[now]:
        indegree[next] -= 1
        res[next]=max(res[next],res[now]+selfBuild[now])
        if indegree[next]==0:
            q.append(next)
for i in range(1,n+1):
    print(res[i]+selfBuild[i])