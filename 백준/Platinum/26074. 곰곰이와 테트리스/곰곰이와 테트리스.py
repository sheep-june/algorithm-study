import sys
input = sys.stdin.readline
n, m = map(int, input().split())
print('ChongChong') if (n == 1 and m == 2) or (n == 2 and m == 1) else print('GomGom')