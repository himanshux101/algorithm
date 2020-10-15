a = [1,2,3,4,5,6,7]

for i in range(len(a)//2):
    a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]

print(a) 