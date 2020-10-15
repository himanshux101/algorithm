from math import factorial

n = 4
k = 14

numbers = [i+1 for i in range(0, n)]
string = ""
k -= 1
for i in range(1, n+1):
    index = k // factorial(n-i)
    print(index)
    string += str(numbers[index])
    del numbers[index]
    print(numbers)
    # k = k - (index * factorial(n-i))
    k = k % factorial(n-i)

print(string)