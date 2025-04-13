import sys
input = sys.stdin.readline

def hanoi(n, fr, tmp, to, k):
    if n == 1:
        if k == 1:
            return (fr, to)
    else:
        half = 2 ** (n - 1) - 1
        if k <= half:
            return hanoi(n - 1, fr, to, tmp, k)
        elif k == half + 1:
            return (fr, to)
        else:
            return hanoi(n - 1, tmp, fr, to, k - half - 1)

a, b = map(int, input().split())
result = hanoi(a, 1, 2, 3, b)
print(result[0], result[1])