fHandle = open("G:\\_\\case\\wbtemp_16097931245830854983160605385390868\\2a7c5618b666132ee8bd8adf4a05846ca5341e2d", "rb")

array = bytearray(fHandle.read())

temp = array[:]


key = bytearray("\x4A\x73\x55\x2F\x55\x47\x55\x6F\x7D\x4A")


for a in range(0, len(array), 10):
    for i in range(0, len(key)):
        if (i+a)>= len(array):
            break;
        temp[i+a] = temp[i+a] ^ key[i%len(key)]

fHandle.close()
fHandle = open("temp.txt", "wb")
fHandle.write(temp)
fHandle.close()
