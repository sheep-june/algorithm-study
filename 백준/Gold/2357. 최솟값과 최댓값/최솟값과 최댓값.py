import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

treeHeight = 0
length = n
while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
treeMin = [sys.maxsize] * (treeSize + 1)
treeMax = [0] * (treeSize + 1)

for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + n + 1):
    value = int(input())
    treeMin[i] = value
    treeMax[i] = value

def setTree():
    for i in range(leftNodeStartIndex, 0, -1):
        treeMin[i] = min(treeMin[i * 2], treeMin[i * 2 + 1])
        treeMax[i] = max(treeMax[i * 2], treeMax[i * 2 + 1])

setTree()

def getMin(s, e):
    minValue = sys.maxsize
    while s <= e:
        if s % 2 == 1:
            minValue = min(minValue, treeMin[s])
            s += 1
        if e % 2 == 0:
            minValue = min(minValue, treeMin[e])
            e -= 1
        s //= 2
        e //= 2
    return minValue

def getMax(s, e):
    maxValue = 0
    while s <= e:
        if s % 2 == 1:
            maxValue = max(maxValue, treeMax[s])
            s += 1
        if e % 2 == 0:
            maxValue = max(maxValue, treeMax[e])
            e -= 1
        s //= 2
        e //= 2
    return maxValue

for _ in range(m):
    s, e = map(int, input().split())
    s = s + leftNodeStartIndex
    e = e + leftNodeStartIndex
    print(getMin(s, e), getMax(s, e))
