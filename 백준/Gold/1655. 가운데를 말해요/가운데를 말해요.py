import sys
import heapq

input = sys.stdin.readline
n = int(input())
lt, rt = [], []

for _ in range(n):
    num = int(input())
    if len(lt) == 0 or -lt[0] >= num:
        heapq.heappush(lt, -num)
    else:
        heapq.heappush(rt, num)

    if len(lt) > len(rt) + 1:
        heapq.heappush(rt, -heapq.heappop(lt))
    elif len(rt) > len(lt):
        heapq.heappush(lt, -heapq.heappop(rt))

    print(-lt[0])
