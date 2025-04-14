import sys

input = sys.stdin.readline

n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=[]
for i in range(1,n):
    b.append(a[i]-a[i-1])
b.sort(reverse=True)

print(sum(b[k-1:]))