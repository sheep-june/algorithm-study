import sys
input = sys.stdin.readline
d=[[0 for j in range(1001)]for i in range(1001)]
n,m=map(int,input().split())
MAX=0
for i in range(0,n):
    numbers=list(input())
    for j in range(0,m):
        d[i][j]=int(numbers[j])
        if d[i][j]==1 and j>0 and i>0:
            d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
            # d[i][j]=min(d[i-1][j-1],d[i-1][j],d[i][j-1]+d[i][j])
        if MAX<d[i][j]:
            MAX=d[i][j]
print(MAX*MAX)