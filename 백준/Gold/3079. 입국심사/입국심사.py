import sys
input = sys.stdin.readline

def c_process(max_time, times, M):
    total_people = 0
    for time in times:
        total_people += max_time // time
        if total_people >= M:  # Early stopping if we can already process all people
            return True
    return total_people >= M

n,m=map(int, input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()
lt = a[0]
rt = a[-1]*m
while lt<=rt:
    mid = (lt + rt)//2
    if c_process(mid,a,m):
        result = mid
        rt = mid-1
    else:
        lt = mid+1

print(result)