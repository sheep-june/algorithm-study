import sys

# from collections import deque
input = sys.stdin.readline
a=input().strip()
b=input().strip()
dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(0, len(a)):
    for j in range(0, len(b)):
        if a[i] == b[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(dp[-1][-1])