# import math
# import copy
import sys
# from sys import *
# import heapq
# sys.setrecursionlimit(10 ** 5)
from collections import *
# from queue import *

input = sys.stdin.readline
print=sys.stdout.write
n=int(input())
tree=[[]for _ in range(n+1)]
for _ in range(0,n-1):
    s,e=map(int,input().split())
    tree[s].append(e)
    tree[e].append(s)
depth=[0]*(n+1)
parent=[0]*(n+1)
visited=[False]*(n+1)
def bfs(node):
    q=deque()
    q.append(node)
    visited[node]=True
    level=1
    now_size=1
    count=0
    while q:
        now_node=q.popleft()
        for next in tree[now_node]:
            if not visited[next]:
                visited[next]=True
                q.append(next)
                parent[next]=now_node
                depth[next]=level
        count+=1
        if count==now_size:
            count=0
            now_size=len(q)
            level+=1
bfs(1)
def executeLCA(a,b):
    if depth[a]<depth[b]:
        temp=a
        a=b
        b=temp
    while depth[a] != depth[b]:
        a=parent[a]
    while a!= b:
        a=parent[a]
        b=parent[b]
    return a
m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    print(str(executeLCA(a,b)))
    print("\n")