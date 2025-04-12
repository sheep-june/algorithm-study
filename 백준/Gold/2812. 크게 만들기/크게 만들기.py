import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().strip()))
stack = []

for num in a:
    while m > 0 and stack and stack[-1] < num:
        stack.pop()
        m -= 1
    stack.append(num)

stack = stack[:-m] if m > 0 else stack

for num in stack:
    print(num, end='')
