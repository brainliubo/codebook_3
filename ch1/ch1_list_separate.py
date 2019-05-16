# 利用*号进行列表的分解
item = [1,2,3,20,23]
a,*b = item
print(a,sum(b))


item1 = [ ("foo",1,2), ("bar",3,4), ("foo",6,5)]
for name, *value in item1:
    if name == "foo":
        print(value)
