# import math
import copy
import sys
import heapq
# sys.setrecursionlimit(10 ** 5)
# from collections import *
# from queue import *

input = sys.stdin.readline
n=int(input())
pq=[]
sum=0
for i in range(n):
    tempc=list(input())
    for j in range(n):
        temp=0
        if 'a' <= tempc[j]<='z':
            temp=ord(tempc[j])-ord('a')+1
        elif 'A' <= tempc[j]<='Z':
            temp=ord(tempc[j])-ord('A')+27
        sum += temp
        if i != j and temp != 0:
            heapq.heappush(pq, (temp,i,j))
parent=[0]*n
for i in range(n):
    parent[i]=i
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
useEdge=0
result=0

while pq:
    v,s,e=heapq.heappop(pq)
    if find(s) != find(e):
        union(s,e)
        result += v
        useEdge += 1
if useEdge==n-1:
    print(sum-result)
else:
    print(-1)