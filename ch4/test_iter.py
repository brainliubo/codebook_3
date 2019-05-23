
class Node():
    def __init__(self,value):
        self.value = value
        self._children = []

    def __iter__(self):
        return iter(self._children)
    def add_node(self,node):
        self._children.append(node)

   # 如果要Print 对象，则需要定义__repr__函数或者str 函数
    def __repr__(self):
        return "Node ({!r})".format(self.value)


if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_node(child1)
    root.add_node(child2)
    for ch in root:
        print(ch)