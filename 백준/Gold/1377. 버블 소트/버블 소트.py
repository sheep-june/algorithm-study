import sys

# from collections import deque
input = sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    a.append((int(input()),i))
MAX=0
sortedA=sorted(a)
for i in range(n):
    if MAX < sortedA[i][1]-i:
        MAX=sortedA[i][1]-i
print(MAX+1)