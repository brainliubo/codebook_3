def fgen(start,stop,inc):
    x = start
    while x < stop:
        yield x
        x += inc


if __name__ == "__main__":
    for i in fgen(10,100,3):
        print(i)