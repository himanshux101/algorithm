a = [5,4,3,2,1]
b = []
c = []

def hanoi(n, source, spare, target):
    if n > 0:
        hanoi(n-1, source, target, spare)
        target.append(source.pop())
        hanoi(n-1, spare, source, target)

hanoi(5, a, b , c)
print(a, b, c)