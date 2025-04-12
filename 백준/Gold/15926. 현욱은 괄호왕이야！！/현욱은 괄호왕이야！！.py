import sys
input = sys.stdin.readline
n=int(input())
a=input().strip()
stack=[]
check=-1
MAX=0
for i in range(n):
    if a[i]=='(':
        stack.append(i) #인덱스값을 저장
    else:
        if stack:
            stack.pop() # 스택에서 하나 팝하여 괄호 쌍을 완성
            if stack:   # 스택이 비어있지 않으면, 최근 열린 괄호와 쌍을 이룸
                MAX=max(MAX, i-stack[-1])# 스택의 마지막 요소 다음 인덱스부터 현재 인덱스까지의 길이
            else:       # 스택이 비었다면, 기본 포인트부터 현재 인덱스까지의 길이
                MAX=max(MAX,i-check)
        else:           #체크포인트를 업데이트
            check=i 
print(MAX)