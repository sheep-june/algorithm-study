import sys
input = sys.stdin.readline

a=list(input().strip())
b=list(input().strip())
while len(b)>=len(a):
    if a==b:
        print(1)
        sys.exit()
    if b[-1]=='B':
        b.pop()
        b=b[::-1]
    else:
        b.pop()
print(0)