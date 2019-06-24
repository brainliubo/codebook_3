class person:
    def __init__(self,first_name):
        self._first_name = first_name

    # getter 函数
    @property
    def first_name(self):
        return  self._first_name

    #setter 函数
    @first_name.setter
    def first_name(self,var):
        if not isinstance(var,str):  # 检查输入的值是什么
            raise TypeError("Expect a string")
        self._first_name = var

    #deleter 函数
    @first_name.deleter
    def first_name(self):
        raise AttributeError("can't delete attribute")


if __name__ == "__main__":
    a = person("liubo")
    print(a.first_name)
    a.first_name= 42
    del a.first_name
