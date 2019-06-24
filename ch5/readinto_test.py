import array
a = array.array("i",[0,0,0,1,1,1,2,2,2])
with open("data.bin","rb") as f:
    f.readinto(a)

