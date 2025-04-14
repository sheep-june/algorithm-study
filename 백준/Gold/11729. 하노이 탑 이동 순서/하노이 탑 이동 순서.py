count=0
memo= []
def hanoi_tower1(n,fr,tmp,to):
    global count
    if n==1:
        memo.append((fr, to))
        count += 1
    else:
        hanoi_tower1(n-1,fr,to,tmp)
        memo.append((fr, to))
        count += 1
        hanoi_tower1(n-1, tmp, fr, to)

n=int(input())
hanoi_tower1(n,1,2,3)
print(count)
for pair in memo:
    print(pair[0], pair[1])