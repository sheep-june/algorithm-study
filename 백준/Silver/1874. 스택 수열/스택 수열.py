#스택클래스
class ArrayStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1
        self.operation = []
    def isEmpty(self): return self.top == -1
    def isFull(self): return self.top == self.capacity - 1
    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.operation.append('+')
            self.array[self.top] = item
        else: pass
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            self.operation.append('-')
            return self.array[self.top+1]
        else: pass
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: return -1
    def size(self):
        return self.top + 1

n=int(input())
stack=ArrayStack(100000)
listnum=[0]
for i in range(n):
    s = int(input())
    listnum.append(s)
count=1
success= True
for i in range(1,n+1):
    #숫자증가->push
    if listnum[i]>listnum[i-1]:
        for s in range(listnum[i]-(count-1)):
            stack.push(count)
            count += 1
        if stack.peek()!=listnum[i]:
            success=False
            break
        else:
            stack.pop()
    #숫자감소->pop
    elif listnum[i]<listnum[i-1]:
        if stack.peek() != listnum[i]:
            success=False
            break
        else:
            stack.pop()
if success:
    print('\n'.join(stack.operation))
else:
    print("NO")