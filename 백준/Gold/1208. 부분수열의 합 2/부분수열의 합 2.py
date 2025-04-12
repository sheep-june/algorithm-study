import sys
import itertools
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
sub_1 = []
sub_2 = []
cnt = 0

for i in range(n//2 + 1):
    for j in itertools.combinations(arr[:n//2], i):
        sub_1.append(sum(j))
    lt_len = len(sub_1)
    sub_1.sort()
for i in range(n - n//2 + 1):
    for j in itertools.combinations(arr[n//2:], i):
        sub_2.append(sum(j))
    rt_len = len(sub_2)
    sub_2.sort(reverse=True)

l, r = 0, 0
cnt = 0

while l < lt_len and r < rt_len:
    curr_left, curr_right = sub_1[l], sub_2[r]
    curr_sum = sub_1[l] + sub_2[r]

    if curr_sum == s:
        ls = l
        rs = r
        while ls < lt_len and sub_1[ls] == curr_left:
            ls += 1
        while rs < rt_len and sub_2[rs] == curr_right:
            rs += 1
        cnt += (ls - l) * (rs - r)
        l, r = ls, rs
    elif curr_sum < s:
        l += 1
    elif curr_sum > s:
        r += 1

print(cnt-1 if s == 0 else cnt)