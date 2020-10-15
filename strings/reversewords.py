sentence = 'this is a good thing to start doing'

some = sentence.split(" ")

print(some)
print(sentence)

var = ""
for i in range(len(some)):
    var += some.pop() + " "

print(var)