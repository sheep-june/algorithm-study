import sys
import math
input = sys.stdin.readline

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = int(input())

dp = [[0] * 14 for _ in range(n + 1)]
mod = 10007

dp[0][0] = 1
for i in range(n):
    for j in range(13):
        for k in range(4):
            if i + k <= n:
                dp[i + k][j + 1] += dp[i][j] * combination(4, k)
idx = 1
ans = 0
# 가능한 만큼 포카드의 쌍을 채운다
while 4 * idx <= n:
    temp = combination(13, idx)
    ans += temp * dp[n - 4 * idx][13 - idx]
    ans %= mod
    idx += 1
    
# 정답출력
print(ans % mod)