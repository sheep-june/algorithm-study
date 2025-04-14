import sys
input = sys.stdin.readline


n=int(input())
a=list(map(int,input().split()))
stack=[]
ans=[]
for i in range(n):
    while stack:
        if stack[-1][1] > a[i]:
            ans.append(stack[-1][0])
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append((i+1,a[i]))
for num in ans:
    print(num,end=' ')