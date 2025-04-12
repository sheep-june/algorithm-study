import sys
input = sys.stdin.readline

K = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

SUMA = []
for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += A[j]
        SUMA.append(sum)

SUMB = {}
for i in range(M):
    sum = 0
    for j in range(i, M):
        sum += B[j]
        if sum in SUMB:
            SUMB[sum] += 1
        else:
            SUMB[sum] = 1

res = 0
for a in SUMA:
    t = K - a
    if t in SUMB:
        res += SUMB[t]

print(res)
