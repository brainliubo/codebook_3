from collections import namedtuple

a = ("www.baidu.com","192.168.12.11",80,89)

wangzhi = namedtuple("wangzhi",["addr","ip","port","port1"])
b = wangzhi(*a)  # 这需要使用a 的不同参数进行初始化
print(b.addr)
print(b.ip)
print(b.port1)