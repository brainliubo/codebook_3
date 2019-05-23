#tb_size cal

def tb_size_cal(tb_size):
    if(tb_size > 6144):
        c = (tb_size + (6144-24-1))//(6144-24)
        print("c = {} ".format(c))
        b_post = tb_size + c * 24
        print("b_post= {}".format(b_post))

        k = b_post //c
        kadd = k*c
        print("k ={}".format(k))
        print("kadd = {}".format(kadd))

        if (k <= 512) and (k >=40):
            step = 8
        elif (k > 512) and (k <= 1024):
            step = 16
        elif (k > 1024) and (k <= 2048):
            step = 32
        else:
            step = 64

        a = k//step
        b = k%step
        if (b != 0):
            kadd = (a+1)*step
        else:
            kadd = a * step

        c_min = (c * kadd - b_post)//step
        c_max = c-c_min

        print("tb_size = {},total cb size = {}".format(tb_size,b_post))
        print("c = {},c_min = {},k_min = {},c_max ={},kadd = {}".format(
            c,c_min,k,c_max,kadd
        ))

if __name__ == "__main__":
    tb_size_cal(75536)