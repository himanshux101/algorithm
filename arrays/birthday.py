people = [[0,0,1,0], [0,0,1,0], [0,0,0,0], [0,0,1,0]]

def find_celeb(people):
    candidate = 0

    for i in range(1, len(people)):
        if people[candidate][i] == 1:
            candidate = i
    
    for i in range(len(people)):
        if i != candidate and people[i][candidate] != 1:
            return -1
    return candidate

print(find_celeb(people))