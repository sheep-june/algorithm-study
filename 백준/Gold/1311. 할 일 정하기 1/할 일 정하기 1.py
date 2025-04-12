import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [10**6] * (1 << n)
dp[0] = 0

def count_set_bits(state):
    count = 0
    while state > 0:
        count += state % 2
        state //= 2
    return count

for i in range(1 << n):
    k = count_set_bits(i)
    for j in range(n):
        if (i // (2 ** j)) % 2 == 0 and dp[i + (2 ** j)] > dp[i] + cost[k][j]:
            dp[i + (2 ** j)] = dp[i] + cost[k][j]

print(dp[-1])
