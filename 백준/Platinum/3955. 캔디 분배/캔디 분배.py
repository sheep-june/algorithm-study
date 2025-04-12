import sys

input = sys.stdin.readline

def gcd(a, b, k):
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while b!= 0:
        q = a//b
        r = a%b;
        a = b
        b = r
        s = s0 - q*s1
        t = t0 - q*t1
        s0 = s1
        s1 = s
        t0 = t1
        t1 = t
    t0 = (t0 % k + k) % k
    if a != 1 or t0 > 10**9:
        return "IMPOSSIBLE"
    return t0

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if b == 1:
        if a+1 > 10**9:
            print("IMPOSSIBLE")
        else:
            print(a+1)
        continue
    if a == 1:
        print(1)
        continue
    res = gcd(a, b, a)
    print(res)