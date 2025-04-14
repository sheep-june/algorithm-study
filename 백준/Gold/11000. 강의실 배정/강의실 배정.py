import sys
input = sys.stdin.readline

n = int(input())
start = []
end = []

for _ in range(n):
    a, b = map(int, input().split())
    start.append(a)
    end.append(b)

start.sort()
end.sort()

i = 0
j = 0
cnt = 0
res = 0

while i < n:
    if start[i] < end[j]:
        cnt += 1
        i += 1
    else:
        cnt -= 1
        j += 1
    if cnt > res:
        res = cnt

print(res)