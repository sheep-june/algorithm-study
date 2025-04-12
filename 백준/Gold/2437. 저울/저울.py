import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
t=1
for i in arr:
    if t<i:
        break
    t+=i
print(t)