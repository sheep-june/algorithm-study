n, s = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

lt=0
rt=0
sum = 0
min_length=1e9

while True:
    if sum >= s:
        min_length=min(min_length,rt-lt)
        sum -= nums[lt]
        lt +=1
    elif rt == n:
        break
    else:
        sum += nums[rt]
        rt+=1

if min_length == 1e9:
    print(0)
else:
    print(min_length)