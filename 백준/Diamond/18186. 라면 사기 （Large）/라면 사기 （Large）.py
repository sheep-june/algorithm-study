import sys

# from collections import deque
input = sys.stdin.readline


def buy(index, seq, count=1):
    global cost

    for i in range(seq):
        nums[index + i] -= count

    to_spend = costs[seq - 1]
    if seq == 3:
        if costs[0] * 3 < costs[2]:
            to_spend = costs[0] * 3
        elif costs[1] + costs[0] < costs[2]:
            to_spend = costs[1] + costs[0]
    elif seq == 2 and costs[0] * 2 < costs[1]:
        to_spend = costs[0] * 2
    cost += to_spend * count


def sol():
    global cost

    f23 = costs[2] + costs[0] * 2 > costs[1] + costs[2]
    f22 = costs[2] + costs[0] > costs[1] * 2

    cost = 0
    i = 0
    while i < n:
        if nums[i] == 0:
            i += 1
        else:
            min2 = min(nums[i:i + 2]) if i + 1 < n else False
            min3 = min(min2, nums[i + 2]) if i + 2 < n else False
            min4 = min(min3, nums[i + 3]) if i + 3 < n else False

            if f23 and i + 3 < n and nums[i + 1] > nums[i + 2] and nums[i + 3] >= 1:
                minn = min(nums[i], nums[i + 1], nums[i + 1] - nums[i + 2])
                buy(i, 2, 1 if minn <= 2 else minn - 2)
            elif f22 and i + 3 < n and min4 >= 1:
                buy(i, 2, 1 if min4 <= 2 else min4 - 2)

            elif i + 2 < n and min3 >= 1:
                buy(i, 3, 1 if min3 <= 2 else min3 - 2)
            elif i + 1 < n and min2 >= 1:
                buy(i, 2, 1 if min2 <= 2 else min2 - 2)
            else:
                buy(i, 1, 1 if nums[i] <= 2 else nums[i] - 2)
    return cost
n, b, c = map(int, input().split())
costs = [b, b + c, b + c * 2]
nums = list(map(int, input().split()))
print(sol())