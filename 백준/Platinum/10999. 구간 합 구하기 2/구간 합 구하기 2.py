import sys
import math
input = sys.stdin.readline

def glen():
    if n & (n-1) == 0:
        return 2*n
    else:
        return pow(2, math.ceil(math.log(n, 2)) + 1)

def init(idx, st, ed):
    if st == ed:
        seg[idx] = num[st]
        return
    mid = (st + ed) // 2
    init(idx*2, st, mid)
    init(idx*2+1, mid+1, ed)
    seg[idx] = seg[idx*2] + seg[idx*2+1]

def upd(idx, st, ed, l, r, val):
    prop(idx, st, ed)
    if r < st or ed < l:
        return
    if l <= st and ed <= r:
        seg[idx] += (ed - st + 1) * val
        if st != ed:
            laz[idx*2] += val
            laz[idx*2+1] += val
        return
    mid = (st + ed) // 2
    upd(idx*2, st, mid, l, r, val)
    upd(idx*2+1, mid+1, ed, l, r, val)
    seg[idx] = seg[idx*2] + seg[idx*2+1]

def qry(idx, st, ed, l, r):
    prop(idx, st, ed)
    if r < st or ed < l:
        return 0
    if l <= st and ed <= r:
        return seg[idx]
    mid = (st + ed) // 2
    return qry(idx*2, st, mid, l, r) + qry(idx*2+1, mid+1, ed, l, r)

def prop(idx, st, ed):
    if laz[idx] != 0:
        seg[idx] += (ed - st + 1) * laz[idx]
        if st != ed:
            laz[idx*2] += laz[idx]
            laz[idx*2+1] += laz[idx]
        laz[idx] = 0

n, m, k = map(int, input().split())
num = [-1] + [int(input()) for _ in range(n)]

tlen = glen()
seg = [0] * tlen
laz = [0] * tlen
init(1, 1, n)

for _ in range(m + k):
    cur = list(map(int, input().split()))
    if cur[0] == 1:
        _, b, c, d = cur
        upd(1, 1, n, b, c, d)
        
    else:
        _, b, c = cur
        print(qry(1, 1, n, b, c))
        
