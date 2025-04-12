import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

def preorder(i_s, i_e, p_s, p_e):
    if(i_s > i_e) or (p_s > p_e):
        return

    parents = postorder[p_e]
    print(parents, end=" ")

    lt = position[parents] - i_s
    rt = i_e - position[parents]

    preorder(i_s, i_s+lt-1, p_s, p_s+lt-1)
    preorder(i_e-rt+1, i_e, p_e-rt, p_e-1) 

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0]*(n+1)
for i in range(n):
    position[inorder[i]] = i

preorder(0, n-1, 0, n-1)