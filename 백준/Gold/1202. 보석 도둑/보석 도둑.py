import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
a = []
for _ in range(n):
    heapq.heappush(a, list(map(int, input().split())))
bag = []
for _ in range(k):
    bag.append(int(input()))
bag.sort()

res = 0
jew = []
for num in bag:
    while a and num >= a[0][0]:
        heapq.heappush(jew, -heapq.heappop(a)[1])
    if jew:
        res -= heapq.heappop(jew)
    elif not a:
        break
print(res)