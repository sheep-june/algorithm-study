import sys
# from collections import deque
input = sys.stdin.readline

res=[]
stack=[]
n=input().strip()
for char in n:
    if char =='+' or char=='-':
        while stack and stack[-1] in ['+', '-', '*', '/']:
            res.append(stack.pop())
        stack.append(char)
    elif char =='*' or char=='/':
        while stack and stack[-1] in ['*', '/']:
            res.append(stack.pop())
        stack.append(char)
    elif char=='(':
        stack.append(char)
    elif char==')':
        while stack and stack[-1] != '(':
            res.append(stack.pop())
        stack.pop()
    else:
        res.append(char)
while stack:
    res.append(stack.pop())
for ch in res:
    print(ch,end='')