from itertools import chain
x = {1,2,4}
y = [1,3,4]


for i in chain(x,y):
    print(i+5)