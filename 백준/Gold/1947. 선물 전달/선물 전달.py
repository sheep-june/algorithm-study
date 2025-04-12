import sys

input = sys.stdin.readline
n=int(input())
mod=1000000000
d=[0]*1000001
d[1]=0
d[2]=1
for i in range(3,n+1):
    d[i]=(i-1)*(d[i-1]+d[i-2])%mod
print(d[n])