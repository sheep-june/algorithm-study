import sys

# from collections import deque
input = sys.stdin.readline
n=int(input())
bricks=[]
for i in range(n):
    s,h,w=map(int,input().split())
    bricks.append((s,h,w,i+1))
dp=[0]*n
bricks.sort(reverse=True)
dp[0]=bricks[0][1]
parent = [-1] * n
for i in range(1,n):
    maxh=0
    for j in range(i-1,-1,-1):
        if bricks[j][2]>bricks[i][2] and dp[j]>maxh:
            maxh=dp[j]
    dp[i]=maxh+bricks[i][1]

max_height = max(dp)

max_index = dp.index(max_height)
result = []
while max_index != -1:
    result.append(bricks[max_index][3])  
    new_maxh = 0
    new_idx = -1
    for k in range(max_index):
        if bricks[k][2] > bricks[max_index][2] and dp[k] > new_maxh:
            new_maxh = dp[k]
            new_idx = k
    max_index = new_idx

print(len(result))
for num in result:
    print(num)