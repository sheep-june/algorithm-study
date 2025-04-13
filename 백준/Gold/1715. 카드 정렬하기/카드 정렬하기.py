import sys
import heapq

input = sys.stdin.readline
n = int(input())
hq = [int(input()) for _ in range(n)]
heapq.heapify(hq)
res = 0
while len(hq) > 1:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    res += a + b
    heapq.heappush(hq, a+b)

print(res)