import math
import sys
# sys.setrecursionlimit(10000)
# from collections import deque
# from queue import PriorityQueue
input = sys.stdin.readline
MIN,MAX=map(int,input().split())
ch=[False]*(MAX-MIN+1)
for i in range(2,int(math.sqrt(MAX)+1)):
    pow=i*i
    lt=int(MIN/pow)
    if MIN % pow!=0:
        lt += 1
    for j in range(lt,int(MAX/pow)+1):
        ch[int((j*pow)-MIN)]=True
cnt = 0
for i in range(0,MAX-MIN+1):
    if not ch[i]:
        cnt += 1
print(cnt)