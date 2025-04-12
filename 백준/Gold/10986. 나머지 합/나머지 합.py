import sys
input = sys.stdin.readline


n,m=map(int,input().split())
numbers = list(map(int, input().split()))
sum_list=[]
sum=0
count=0
for num in numbers:
	sum += num
	k = sum%m
	sum_list.append(k)
r_list=[0]*m
for num in sum_list:
	r_list[num] += 1
zero_count = sum_list.count(0)
count += zero_count
for r in r_list:
	if r>1:
		count += (r*(r-1))//2

print(count)