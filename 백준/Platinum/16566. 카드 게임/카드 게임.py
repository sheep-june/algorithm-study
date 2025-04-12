from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
c_number = list(map(int, input().strip().split()))
s_card = list(map(int, input().strip().split()))
visited = [False] * (len(c_number) + 1)

c_number.sort()
for card in s_card:
    r_idx = bisect_right(c_number, card)
    while True:
        if not visited[r_idx]:
            visited[r_idx] = True
            print(c_number[r_idx])
            break
        else:
            r_idx += 1