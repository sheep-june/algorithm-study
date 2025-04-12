import math
import sys
# sys.setrecursionlimit(10000)
# from collections import deque
# from queue import PriorityQueue
input = sys.stdin.readline
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def dfs(v):
    ch[v]=True
    for i in A[v]:
        next=i[0]
        if not ch[next]:
            d[next]=d[v]*i[2]//i[1]
            dfs(next)
n=int(input())
A=[[]for _ in range(n)]
ch=[False]*n
d=[0]*n
lcm=1
for i in range(n-1):
    a,b,p,q=map(int,input().split())
    A[a].append((b,p,q))
    A[b].append((a,q,p))
    lcm *= (p*q//gcd(p,q))
d[0]=lcm
dfs(0)
mgcd=d[0]
for i in range(1,n):
    mgcd=gcd(mgcd,d[i])
for i in range(n):
    print(d[i]//mgcd,end=' ')