import sys
input = sys.stdin.readline

memo = {}
n = int(input())
for i in range(n):
    strr = list(input().strip())
    for j in range(len(strr)-1, -1, -1):
        chrr = strr[len(strr)-1 - j]
        if chrr in memo:
            memo[chrr] += 10 ** j
        else:
            memo[chrr] = 10 ** j
memo = dict(sorted(memo.items(), key=lambda x: x[1], reverse=True))
num = 9
res = 0
for c in memo:
    res += memo[c] * num
    num -= 1
print(res)