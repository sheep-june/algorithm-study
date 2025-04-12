import math
import sys
# sys.setrecursionlimit(10000)
# from collections import deque
# from queue import PriorityQueue
input = sys.stdin.readline
n=int(input())
res=n
for p in range(2,int(math.sqrt(n))+1):
    if n%p==0:
        res -= res/p
        while n%p==0:
            n /= p
if n>1:
    res -= res/n
print(int(res))