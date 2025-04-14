import sys

# from collections import deque
input = sys.stdin.readline
n=int(input())
t=[0]*(n+1)
p=[0]*(n+1)
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())
dp=[0]*(n+1)

for i in range(1,n+1):
    dp[i]=max(dp[i],dp[i-1])
    now=i+t[i]-1
    if now <=n:
        dp[now]=max(dp[now],dp[i-1]+p[i])
print(max(dp))