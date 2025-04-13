import sys
input = sys.stdin.readline

def dfs(depth):
    global n, res

    if depth == n:
        res += 1
        return

    for i in range(n):
        if not col[i] and not up[depth + i] and not down[(n - 1) + depth - i]:
            col[i] = 1
            up[depth + i] = 1
            down[(n - 1) + depth - i] = 1
            dfs(depth + 1)
            col[i] = 0
            up[depth + i] = 0
            down[(n - 1) + depth - i] = 0

n = int(input())
col = [0] * n
up = [0] * (2 * (n - 1) + 1)
down = [0] * (2 * (n - 1) + 1)

res = 0

dfs(0)
print(res)
