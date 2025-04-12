import sys
input = sys.stdin.readline


def dfs(string):
    l = len(string)
    pi = [0]*l
    j = 0

    for i in range(1, l):
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]

        if string[i] == string[j]:
            j += 1
            pi[i] = j

    return L - pi[-1]


L = int(input())
s = str(input().rstrip())
print(dfs(s))