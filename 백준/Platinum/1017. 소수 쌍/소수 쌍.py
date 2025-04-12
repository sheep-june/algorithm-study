import sys
input = sys.stdin.readline
import math


def dfs(t):
    global y
    global matched
    global visited
    if visited[y.index(t)]: return False
    visited[y.index(t)] = True
    for s in y:
        if t + s in primes:
            if s not in matched or dfs(matched[s]):
                matched[s] = t
                return True
    return False

n = int(input())
x = list(map(int, input().split()))

primes = []
for i in range(2, 2000):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        continue

answers = []
for i in x:
    matched = {}
    if i == x[0]: continue
    if x[0] + i in primes:
        if n == 2:
            answers.append(i)
            break
        y = [a for a in x]
        del y[0]
        del y[y.index(i)]
        matched = {}
        for b in y:
            visited = [False for _ in range(len(y))]
            dfs(b)

    if n != 2 and len(matched) == n - 2:
        answers.append(i)

if not answers:
    answers.append(-1)

answers.sort()

for num in answers:
    print(num,end=' ')