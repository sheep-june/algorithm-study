import sys
import heapq
input = sys.stdin.readline

n = int(input())
res = []
for i in range(n):
    res.append(list(map(int, input().split())))

res.sort(key=lambda x: (x[1]))
money = []
for i in res:
    heapq.heappush(money, i[0])
    if len(money) > i[1]:
        heapq.heappop(money)
print(sum(money))
