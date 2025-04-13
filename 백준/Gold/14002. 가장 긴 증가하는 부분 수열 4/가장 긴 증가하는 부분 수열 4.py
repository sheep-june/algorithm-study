import sys

# from collections import deque
input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
dp=[0]*(n+1)
dp[1]=1
res=dp[1]
prev = [-1] * (n + 1)
for i in range(2,n+1):
    MAX=0
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dp[j]>MAX:
            MAX=dp[j]
            prev[i] = j
    dp[i]=MAX+1
    if dp[i]>res:
        res=dp[i]
print(res)
lis = []
last = dp.index(res)
while last != -1:
    lis.append(arr[last])
    last = prev[last]

lis.reverse()
for num in lis:
    print(num,end=' ')