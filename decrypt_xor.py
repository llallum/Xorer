fHandle = open("This is the file to be decrypted", "rb")

array = bytearray(fHandle.read())

temp = array[:]


key = bytearray("Here is the key")


for a in range(0, len(array), 10): # 10 is just an example of key length
    for i in range(0, len(key)):
        if (i+a)>= len(array):
            break;
        temp[i+a] = temp[i+a] ^ key[i%len(key)]

fHandle.close()
fHandle = open("temp.txt", "wb")
fHandle.write(temp)
fHandle.close()
