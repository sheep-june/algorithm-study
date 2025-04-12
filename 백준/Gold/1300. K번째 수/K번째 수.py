import sys
# sys.setrecursionlimit(10000)
# from collections import deque
input = sys.stdin.readline
n=int(input())
k=int(input())
lt=1
rt=k
res=0
while lt<=rt:
    mid=(lt+rt)//2
    cnt=0
    for i in range(1,n+1):
        cnt += min(mid//i,n)
    if cnt <k:
        lt=mid+1
    else:
        res=mid
        rt=mid-1
print(res)