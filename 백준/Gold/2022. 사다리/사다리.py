import math
import sys
input = sys.stdin.readline


x, y, c = map(float, input().split())
lt=0
rt=min(x,y)
while rt-lt>1e-4:
    mid = (lt+rt)/2
    hx = math.sqrt(x**2 - mid**2)
    hy = math.sqrt(y**2 - mid**2)
    res = (hx * hy) / (hx + hy)
    if res > c:
        lt = mid
    else:
        rt = mid
print("{:.3f}".format((lt + rt) / 2))