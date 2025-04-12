import sys
import heapq

input = sys.stdin.readline

n = int(input())
hq = []
max_day = 0
for i in range(n):
    d, w = map(int, input().split())
    heapq.heappush(hq, (-w, d))
    if max_day < d:
        max_day = d

assigned = [False] * (max_day + 1)

res = 0
while hq:
    w, d = heapq.heappop(hq)
    w = -w

    for i in range(d, 0, -1):
        if assigned[i]:
            continue

        assigned[i] = True
        res += w
        break

print(res)