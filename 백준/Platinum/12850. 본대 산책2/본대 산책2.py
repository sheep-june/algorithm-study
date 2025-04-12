import sys

input = sys.stdin.readline
mod = 1000000007

d = int(input())

graph = [[0] * 8 for i in range(8)]

graph[0][1] = graph[0][2] = 1
graph[1][0] = graph[1][2] = graph[1][3] = 1
graph[2][0] = graph[2][1] = graph[2][3] = graph[2][4] = 1
graph[3][1] = graph[3][2] = graph[3][4] = graph[3][5] = 1
graph[4][2] = graph[4][3] = graph[4][5] = graph[4][7] = 1
graph[5][3] = graph[5][4] = graph[5][6] = 1
graph[6][5] = graph[6][7] = 1
graph[7][4] = graph[7][6] = 1


def multiply(a, b):
    res = [[0] * 8 for i in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                res[i][j] += a[i][k] * b[k][j]
            res[i][j] %= mod
    return res


def cal(graph, n):
    if n == 1:
        return graph
    cal2 = cal(graph, n // 2)
    if n % 2 == 0:
        return multiply(cal2, cal2)
    else:
        return multiply(multiply(cal2, cal2), graph)


result = cal(graph, d)
print(result[0][0])