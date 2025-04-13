import sys

input = sys.stdin.readline

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

n = int(input())
m = int(input())
city = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0,0)  # 원하는 대로 인덱스를 조정하여 사용하기 위해 추가
route = list(map(int, input().split()))
parent = [0] * (n + 1)
for i in range(1, n+1):
    parent[i] = i
for i in range(1, n+1):
    for j in range(1, n+1):
        if city[i][j] == 1:
            union(i, j)
index = find(route[0])  # 첫 번째 도시를 기준으로 찾기
isConnect = True
for i in range(1, len(route)):
    if index != find(route[i]):
        isConnect = False
        break
if isConnect:
    print("YES")
else:
    print("NO")
