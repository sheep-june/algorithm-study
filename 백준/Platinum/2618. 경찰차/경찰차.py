import sys
input = sys.stdin.readline

def calc(a, b):
    return abs(li[a][0] - li[b][0]) + abs(li[a][1] - li[b][1])
def solve(a, b):
    ret = 0
    next = max(a, b) + 1
    if next == w + 2:
        return 0
    if dp[a][b] != -1:
        return dp[a][b]
    calc1 = solve(next, b) + calc(a, next)
    calc2 = solve(a, next) + calc(b, next)
    if calc1 < calc2:
        ch[a][b] = 1
        dp[a][b] = calc1
    else:
        ch[a][b] = 2
        dp[a][b] = calc2
    ret = dp[a][b]
    return ret

n = int(input())
w = int(input())
li = [[1, 1], [n, n]]
for _ in range(w):
    li.append(list(map(int, input().split())))

dp = [[-1] * (w+2) for _ in range(w+2)]
ch = [[-1] * (w+2) for _ in range(w+2)]
a=0
b=1
print(solve(a,b))
for i in range(2,w+2):
    print(ch[a][b])
    if ch[a][b]==1:
        a=i
    else:
        b=i