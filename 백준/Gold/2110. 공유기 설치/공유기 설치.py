import sys
input = sys.stdin.readline
def check(arr,m,mid):
    last = arr[0]
    count = 1
    for i in range(1,len(arr)):
        if arr[i]-last >= mid:
            count +=1
            last = arr[i]
            if count==m:
                return True
    return False

n,m=map(int, input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()
lt = 1
rt = a[-1]-a[0]
res=0
while lt<=rt:
    mid = (lt + rt)//2
    if check(a,m,mid):
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)