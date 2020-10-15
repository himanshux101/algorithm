ele = ['01', '01', '01']
acc = []
def recur(ele):
    acc_new = list()
    if len(ele) > 2:
        temp = ele[-1]
        ele = recur(ele[:-1])
        ele.append(temp)
    
    acc_new = []
    for i in ele[0]:
        for j in ele[1]:
            acc_new.append(i + j)
    
    return acc_new

print(recur(ele))
        