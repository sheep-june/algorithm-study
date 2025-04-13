import sys
input = sys.stdin.readline

n = int(input())

s_list = list(map(int, input().split()))
up_length = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if s_list[j] < s_list[i]:
            up_length[i] = max(up_length[i],up_length[j]+1)

rs_list = list(reversed(s_list))
down_length = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if rs_list[j] < rs_list[i]:
            down_length[i] = max(down_length[i],down_length[j]+1)
down_length = list(reversed(down_length))

b_sequence = []
for i in range(n):
    b_sequence.append(up_length[i] + down_length[i] - 1)

print(max(b_sequence))