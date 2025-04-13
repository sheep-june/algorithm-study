import sys
input=sys.stdin.readline
import heapq


def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True


t = int(input())

for i in range(t):
    MIN = []
    MAX = []
    nums = dict()
    k = int(input())

    for j in range(k):
        oprt, oprd = input().split()
        num = int(oprd)

        if oprt == 'I':
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
                heapq.heappush(MIN, num)
                heapq.heappush(MAX, -num)

        elif oprt == 'D':
            if not isEmpty(nums.items()):
                if num == 1:
                    while -MAX[0] not in nums or nums[-MAX[0]] < 1:
                        temp = -heapq.heappop(MAX)
                        if temp in nums:
                            del (nums[temp])
                    nums[-MAX[0]] -= 1
                else:
                    while MIN[0] not in nums or nums[MIN[0]] < 1:
                        temp = heapq.heappop(MIN)
                        if temp in nums:
                            del (nums[temp])
                    nums[MIN[0]] -= 1

    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while MIN[0] not in nums or nums[MIN[0]] < 1:
            heapq.heappop(MIN)
        while -MAX[0] not in nums or nums[-MAX[0]] < 1:
            heapq.heappop(MAX)
        print(-MAX[0], MIN[0])