import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())

teleport = {}
for _ in range(N + M):  # 사다리와 뱀을 같은 딕셔너리에 저장
    x, y = map(int, input().strip().split())
    teleport[x] = y

visited = [False] * 101
queue = deque([1])
visited[1] = True
steps = 0

while queue:
    for _ in range(len(queue)):
        current = queue.popleft()

        if current == 100:
            print(steps)
            sys.exit()

        for dice in range(1, 7):
            next_pos = current + dice
            if next_pos <= 100 and not visited[next_pos]:
                visited[next_pos] = True
                # 바로 사다리나 뱀을 통해 이동
                if next_pos in teleport:
                    next_pos = teleport[next_pos]
                    if not visited[next_pos]:
                        visited[next_pos] = True
                        queue.append(next_pos)
                else:
                    queue.append(next_pos)

    steps += 1
