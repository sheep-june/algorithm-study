import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(node):
    visited[node] = 1
    dp[node][0] = 0
    dp[node][1] = 1  
    
    for adj in c[node]:
        if not visited[adj]:
            dfs(adj)
            dp[node][0] += dp[adj][1]  
            dp[node][1] += min(dp[adj][0], dp[adj][1])  

n = int(input())
c = [[] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    c[a].append(b)
    c[b].append(a)

dfs(1)
print(min(dp[1][0], dp[1][1])) 
