from collections import deque
import sys
input = sys.stdin.readline


n,l = map(int,input().split())
dq = deque()
now = list(map(int, input().split()))
for i in range(n):
	#삽입하는것보다 큰 데이터 삭제
	while dq and dq[-1][0] > now[i]:
		dq.pop()
	dq.append((now[i],i))
	#범위 out
	if dq[0][1] <= i-l:
		dq.popleft()
	print(dq[0][0],end=' ')