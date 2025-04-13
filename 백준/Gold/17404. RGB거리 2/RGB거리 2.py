import sys
input = sys.stdin.readline

INF = 1000*1000+1
r, g, b= 0, 1, 2
n=int(input())
cost = [[-1, -1, -1]]
for _ in range(n):
    cost.append(list(map(int, input().rstrip().split())))

ans = INF
for color in [r,g,b]:
    dp = [[-1]*3 for _ in range(n+1)]

    dp[1] = [INF, INF, INF]
    dp[1][color] = cost[1][color]

    for i in range(2, n+1):
        dp[i][r] = min(dp[i-1][g], dp[i-1][b]) + cost[i][r]
        dp[i][g] = min(dp[i-1][r], dp[i-1][b]) + cost[i][g]
        dp[i][b] = min(dp[i-1][r], dp[i-1][g]) + cost[i][b]
    dp[n][color] = INF
    ans = min(ans, min(dp[n]))
print(ans)
