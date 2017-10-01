def parser():
    file = open('webbench', 'rb')
    
    file.seek(0x0, 0)
    str1 = file.read(4)
    file.seek(0x1F68, 0)
    str2 = file.read(8)
    file.seek(0x609c, 0)
    str3 = readSkip(file.read(348))

    print(str1.decode('ascii'))
    print(str2.decode('ascii'))
    print(str3)
    #print(int(str3, 16))

def readSkip(buffer):
    ba = [hex(x) for x in buffer]
    strs = ''
    for x in ba:
        if int(x, 16) <= 0xff:
            
            if int(x, 16) == 0x1 or int(x, 16) == 0x2 or int(x, 16) == 0x3 or int(x, 16) == 0x4 or int(x, 16) == 0x5:
                continue
            strs += chr(int(x, 16))
    return strs;

if __name__ == '__main__':
    parser()
