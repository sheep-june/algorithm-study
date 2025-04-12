import sys
input=sys.stdin.readline
import math

def calc(a, b, c, d):
    return math.sqrt((a-c) ** 2 + (b-d) ** 2)

n = int(input())
pos = []
MIN = 2147000000
x, y = 0, 0
for _ in range(n):
    pos.append(list(map(int, input().split())))

for x1, y1 in pos:
    MAX = 0
    for x2, y2 in pos:
        tmp = calc(x1, y1, x2, y2)
        if MAX < tmp:
            MAX = tmp
    if MIN > MAX:
        MIN = MAX
        x, y = x1, y1

print(x, y)