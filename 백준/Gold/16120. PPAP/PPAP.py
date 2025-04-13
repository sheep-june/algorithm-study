import sys
input = sys.stdin.readline
w = input().strip()
stack = []
ppap = ['P', 'P', 'A', 'P']

for i in range(len(w)):
    stack.append(w[i])
    if len(stack) >= 4 and stack[-4:] == ppap:
        for _ in range(4):
            stack.pop()
        stack.append("P")

if stack == ppap or stack == ['P']:
    print("PPAP")
else:
    print("NP")