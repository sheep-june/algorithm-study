import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

s = input().rstrip()
l = len(s)

dp = [2500 for _ in range(l + 1)]
dp[-1] = 0
p = [[0 for _ in range(l)] for _ in range(l)]

for i in range(l):
    p[i][i] = 1

for i in range(1, l):
    if s[i - 1] == s[i]:
        p[i - 1][i] = 1

for i in range(3, l + 1):
    for start in range(l - i + 1):
        end = start + i - 1
        if s[start] == s[end] and p[start + 1][end - 1]:
            p[start][end] = 1

for end in range(l):
    for start in range(end + 1):
        if p[start][end]:
            dp[end] = min(dp[end], dp[start - 1] + 1)
        else:
            dp[end] = min(dp[end], dp[end - 1] + 1)

print(dp[l - 1])