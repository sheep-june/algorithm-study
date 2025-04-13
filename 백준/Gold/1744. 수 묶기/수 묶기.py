import sys
input = sys.stdin.readline

n = int(input())
yang = []
moo = []
um = []
sum_ones = 0  
for _ in range(n):
    s = int(input())
    if s > 1:
        yang.append(s)
    elif s == 1:
        sum_ones += s  
    elif s == 0:
        moo.append(s)
    else:
        um.append(s)
yang.sort()
um.sort()

sumnum = sum_ones  

if len(um) > 0 and len(um) % 2 == 0:
    sumnum += sum(um[i] * um[i + 1] for i in range(0, len(um), 2))
elif len(um) > 0:
    sumnum += sum(um[i] * um[i+1] for i in range(0, len(um) - 1, 2))
    if moo:
        pass  
    else:
        sumnum += um[-1]  

if len(yang) % 2 == 0:
    sumnum += sum(yang[i] * yang[i + 1] for i in range(0, len(yang), 2))
else:
    sumnum += sum(yang[i] * yang[i + 1] for i in range(1, len(yang), 2))
    sumnum += yang[0]  

print(sumnum)
