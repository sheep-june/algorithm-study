import sys
input = sys.stdin.readline


n,m=map(int,input().split())

sum_list=[]
for i in range(n):
    a=list(map(int,input().split()))
    num=0
    board = []
    for s in a:
        num += s
        board.append(num)
    sum_list.append(board)
# print(sum_list)
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    # print(sum_list[x1-1][y1-1])
    # print(sum_list[x2 - 1][y2 - 1])
    num=0
    for i in range(x1-1,x2):
        if y1==1:
            num += sum_list[i][y2-1]
        else:
            num += sum_list[i][y2-1]-sum_list[i][y1-2]
    print(num)