from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
    global IsEven
    queue = deque([start])
    visited[start] = True
    ch[start] = 0

    while queue:
        node = queue.popleft()
        for i in a[node]:
            if not visited[i]:
                visited[i] = True
                ch[i] = 1 - ch[node]
                queue.append(i)
            elif ch[node] == ch[i]:
                IsEven = False
                return

n = int(input())

for _ in range(n):
    v, e = map(int, input().split())
    a = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    ch = [-1] * (v+1)
    IsEven = True

    for __ in range(e):
        lt, rt = map(int, input().split())
        a[lt].append(rt)
        a[rt].append(lt)

    for i in range(1, v+1):
        if not visited[i] and IsEven:
            bfs(i)
        if not IsEven:
            break

    print("YES" if IsEven else "NO")
