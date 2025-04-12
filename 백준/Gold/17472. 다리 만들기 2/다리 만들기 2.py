import copy
import sys
import heapq
# sys.setrecursionlimit(10 ** 5)
from collections import *
# from queue import *

input = sys.stdin.readline
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n, m = map(int, input().split())
myMap = [[0 for j in range(m)] for i in range(n)]
visited = [[False for j in range(m)] for i in range(n)]
for i in range(n):
    myMap[i] = list(map(int, input().split()))
sNum = 1
sumlist = list([])
mlist = []

def addNode(i, j, queue):
    myMap[i][j] = sNum
    visited[i][j] = True
    temp = [i, j]
    mlist.append(temp)
    queue.append(temp)

def bfs(i, j):
    queue = deque()
    mlist.clear()
    start = [i, j]
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    myMap[i][j] = sNum
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            while r + tempR >= 0 and r + tempR < n and c + tempC >= 0 and c + tempC < m:
                if not visited[r + tempR][c + tempC] and myMap[r + tempR][c + tempC] != 0:
                    addNode(r + tempR, c + tempC, queue)
                else:
                    break
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1
    return mlist

for i in range(n):
    for j in range(m):
        if myMap[i][j] != 0 and not visited[i][j]:
            tempList = copy.deepcopy(bfs(i, j))
            sNum += 1
            sumlist.append(tempList)

pq = []
for now in sumlist:
    for temp in now:
        r = temp[0]
        c = temp[1]
        now_S = myMap[r][c]
        for d in range(4):
            tempR = dr[d]
            tempC = dc[d]
            blength = 0
            while r + tempR >= 0 and r + tempR < n and c + tempC >= 0 and c + tempC < m:
                if myMap[r + tempR][c + tempC] == now_S:
                    break
                elif myMap[r + tempR][c + tempC] != 0:
                    if blength > 1:
                        heapq.heappush(pq, (blength, now_S, myMap[r + tempR][c + tempC]))  # PriorityQueue에서 heapq로 변경
                    break
                else:
                    blength += 1
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

parent = [0] * sNum
for i in range(len(parent)):
    parent[i] = i

useEdge = 0
result = 0
while pq:
    v, s, e = heapq.heappop(pq)  
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

if useEdge == sNum - 2:
    print(result)
else:
    print(-1)
