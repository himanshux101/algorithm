def countAndSay(n: int) -> str:
    print('ITS ON -> ', n)
    if n == 1:
        return "1"
    
    num = countAndSay(n-1)
    print('return number -> ', num)

    new_string = ""
    freq = 1
    val = num[0]
    for i in range(1, len(str(num))):
        if num[i] == val:
            freq += 1
        else:
            new_string += str(freq) + val
            freq = 1
            val = num[i]
    new_string += str(freq) + val
    return new_string
print(countAndSay(4))
# def recurse(n: str) -> str:
#     if n == "1":
#         return "1"
#     new_string = ""
#     freq = 1
#     val = n[0]
#     for i in range(1, len(str(n))):
#         if n[i] == val:
#             freq += 1
#         else:
#             freq = 0
#             val = i
#             new_string += str(freq) + val
#     if new_string == "":
#         new_string += str(freq) + val
#     return new_string


