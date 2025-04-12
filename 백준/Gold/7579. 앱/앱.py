import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(c) + 1)] for _ in range(n + 1)]
result = sum(c)

for i in range(1, n + 1):
    byte = a[i]
    cost = c[i]

    for j in range(sum(c) + 1):
        if j < cost:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(byte + dp[i - 1][j - cost], dp[i - 1][j])

        if dp[i][j] >= m:
            result = min(result, j)

print(result)
