import sys
input = sys.stdin.readline

MOD = 1000000000

def stair_count(N):
    dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]

    p_two = [1]
    for i in range(1, 10):
        p_two.append(p_two[-1] * 2)

    for i in range(1, 10):
        dp[1][i][p_two[i]] = 1

    for i in range(2, N + 1):
        for j in range(10):
            for k in range(1024):
                if j > 0:
                    dp[i][j][k | p_two[j]] = (dp[i][j][k | p_two[j]] + dp[i-1][j-1][k]) % MOD
                if j < 9:
                    dp[i][j][k | p_two[j]] = (dp[i][j][k | p_two[j]] + dp[i-1][j+1][k]) % MOD

    total = 0
    for j in range(10):
        total = (total + dp[N][j][1023]) % MOD

    return total

N = int(input().strip())
print(stair_count(N))