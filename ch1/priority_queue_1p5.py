import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))  #将(-priority,index,item) 作为元素插入到heaqp中
        self._index += 1

    def pop(self):
       return heapq.heappop(self._queue)[-1]  # heapqpop返回的是一个元组，然后将元组的最后一个元素返回

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return  "item ({!r})".format(self.name)


q = PriorityQueue()
q.push(Item("for31"),3)
q.push(Item("for5"),5)
q.push(Item("for4"),4)
q.push(Item("for3"),3)
q.push(Item("for2"),2)
q.push(Item("for1"),1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

