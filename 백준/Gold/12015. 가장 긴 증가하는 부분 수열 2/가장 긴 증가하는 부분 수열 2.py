import sys
input = sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
dp=[]

for num in a:
    low, high = 0, len(dp) - 1
    while low <= high:
        mid = (low + high) // 2
        if dp[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    if low >= len(dp):
        dp.append(num)
    else:
        dp[low] = num
print(len(dp))