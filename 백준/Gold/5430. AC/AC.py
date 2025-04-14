from collections import deque
import sys

input = sys.stdin.readline

def process_test_case(p, n, arr):
    dq = deque(arr)
    reverse_mode = False
    
    for operation in p:
        if operation == 'R':
            reverse_mode = not reverse_mode
        elif operation == 'D':
            if not dq:
                return "error"
            if reverse_mode:
                dq.pop()
            else:
                dq.popleft()
    
    if reverse_mode:
        dq.reverse()
    
    return "[" + ",".join(map(str, dq)) + "]"

t = int(input().strip())
results = []

for _ in range(t):
    p = input().strip()
    n = int(input().strip())
    arr_input = input().strip()
    if n == 0:
        arr = []
    else:
        arr = list(map(int, arr_input[1:-1].split(',')))
    result = process_test_case(p, n, arr)
    results.append(result)

for result in results:
    print(result)
