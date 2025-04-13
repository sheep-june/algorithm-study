import sys

input = sys.stdin.readline

def dfs(v, sum):
    if sum > n:
        return 0
    if v == m:
        return 1 if sum == n else 0
    if (v, sum) in memo:
        return memo[(v, sum)]
    
    total_count = 0
    for i in range(ea[v] + 1):
        total_count += dfs(v + 1, sum + (i * coin[v]))
    
    memo[(v, sum)] = total_count
    return total_count

n = int(input())
m = int(input())
coin = []
ea = []
for _ in range(m):
    a, b = map(int, input().split())
    coin.append(a)
    ea.append(b)

memo = {}
cnt = dfs(0, 0)
print(cnt)
