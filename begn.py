string = "key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"

string = string.split()

def sort(str):
    if str[:3] == "age":
        return True
    else: 
        return False

string = filter(sort, string)

count = 0
for i in string:
    if int(i[4:].replace(',', '')) >= 50:
        print(i)
        count += 1

print(count)