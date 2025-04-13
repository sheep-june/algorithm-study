import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
maxSafeArea = 0

def spreadVirus(copyLab):
    visited = [[0] * m for _ in range(n)]
    queue = []

    for i in range(n):
        for j in range(m):
            if copyLab[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1

    while queue:
        cy, cx = queue.pop(0)
        for d in range(4):
            yy = cy + dy[d]
            xx = cx + dx[d]
            if 0 <= yy < n and 0 <= xx < m and not visited[yy][xx] and copyLab[yy][xx] == 0:
                visited[yy][xx] = 1
                copyLab[yy][xx] = 2
                queue.append((yy, xx))

    safeArea = 0
    for i in range(n):
        for j in range(m):
            if copyLab[i][j] == 0:
                safeArea += 1
    return safeArea

def Wall(start, count):
    global maxSafeArea
    if count == 3:
        copyLab = [row[:] for row in lab]
        maxSafeArea = max(maxSafeArea, spreadVirus(copyLab))
        return

    for i in range(start, n * m):
        y = i // m
        x = i % m
        if lab[y][x] == 0:
            lab[y][x] = 1
            Wall(i + 1, count + 1)
            lab[y][x] = 0

Wall(0, 0)
print(maxSafeArea)
