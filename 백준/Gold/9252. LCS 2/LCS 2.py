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
lcs = []
i, j = len(a), len(b)
while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
        lcs.append(a[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1

lcs.reverse()
for num in lcs:
    print(num,end='')