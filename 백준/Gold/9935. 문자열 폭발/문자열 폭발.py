import sys
input = sys.stdin.readline
w = input().strip()
bomb = input().strip()
bomb_len = len(bomb) 
stack = []
bomb_list = list(bomb)  
for char in w:
    stack.append(char)
    if len(stack) >= bomb_len:
        if stack[-bomb_len:] == bomb_list:
            stack[-bomb_len:] = []

print(''.join(stack) if stack else "FRULA")
