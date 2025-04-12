import sys

# from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.append(0)
a.append(0)
res = 0
for i in range(n):
    if a[i + 1] > a[i + 2]:
        num = min(a[i], a[i + 1] - a[i + 2])
        a[i] -= num
        a[i + 1] -= num
        res += num * 5

        num = min(a[i], a[i + 1], a[i + 2])
        a[i] -= num
        a[i + 1] -= num
        a[i + 2] -= num
        res += num * 7
    else:
        num = min(a[i], a[i + 1] ,a[i + 2])
        a[i] -= num
        a[i + 1] -= num
        a[i + 2] -= num
        res += num * 7

        num = min(a[i], a[i + 1])
        a[i] -= num
        a[i + 1] -= num
        res += num * 5
    res += a[i]*3
    a[i]=0
print(res)