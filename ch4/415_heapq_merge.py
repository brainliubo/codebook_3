import heapq

x = [2,4,6,8]
y = [1,3,5,7]

for z  in heapq.merge(x,y):
    print(z)