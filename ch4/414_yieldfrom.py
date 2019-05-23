from collections import Iterable

def flatten(item, ignore_type= (str,bytes) ):
    for x in item:
        if isinstance(x,Iterable) and not isinstance(x,ignore_type):
            yield  from flatten(x)
        else:
            yield  x



if __name__ == "__main__":
    item = [[1, 2], [3, 4], [5, 6]]
    print(type(flatten(item)))  #flatten 返回的是一个generator,因此需要使用for 循环访问
    for x in flatten(item):
        print(x)