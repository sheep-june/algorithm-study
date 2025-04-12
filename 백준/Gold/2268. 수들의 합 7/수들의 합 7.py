import sys

input = sys.stdin.readline

n, m = map(int, input().split())

treeHeight = 0
length = n
while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [0] * (treeSize + 1)

def setTree():
    for i in range(leftNodeStartIndex, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

setTree()

def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return partSum

def modify(index, value):
    tree[index] = value
    while index > 1:
        index //= 2
        tree[index] = tree[index * 2] + tree[index * 2 + 1]

for _ in range(m):
    q, b, c = map(int, input().split())
    if q == 1: 
        b = b + leftNodeStartIndex
        modify(b, c)
    elif q == 0: 
        b = b + leftNodeStartIndex
        c = c + leftNodeStartIndex
        if b > c:
            b, c = c, b
        print(getSum(b, c))
