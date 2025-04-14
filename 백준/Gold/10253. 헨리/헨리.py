import sys
input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(int(input())):
    a, b = map(int, input().split())
    x = 1
    while a != 1:
        while b > a * x:
            x += 1
        a = a * x - b
        b = b * x
        k = gcd(a, b)
        a = a // k
        b = b // k
    print(b)
