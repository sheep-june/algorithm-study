import sys
input = sys.stdin.readline
import heapq

k, n = map(int, input().split())
a = list(map(int, input().split()))
heap = []

for idx, p in enumerate(a):
    heapq.heappush(heap,(p, idx))

for i in range(n):
    m, b = heapq.heappop(heap)
    for idx, p in enumerate(a):
        if idx > b:
            break
        num = p * m
        heapq.heappush(heap, (num, idx))

    if i == n-1:
        print(m)