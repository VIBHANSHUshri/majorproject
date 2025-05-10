import binascii

def check_gif_for_flashing_lights(filename):
    try:
        with open(filename, 'rb') as f:
            content = f.read()
    except IOError:
        return False

    hexc = binascii.hexlify(content).decode("utf-8")

    def unsafe():
        return False

    def extension(idx):
        idx += 2
        while True:
            if hexc[idx:idx+2] == 'f9':
                idx += 14
            if hexc[idx:idx+2] == '01':
                s = int(hexc[idx+2:idx+4],16)
                idx += 2 + (s*2)
                return idx
            if hexc[idx:idx+2] == 'ff':
                s = int(hexc[idx+2:idx+4],16)
                idx += 2 + (s*2)
                return idx
            if hexc[idx:idx+2] == 'fe':
                idx += 2
                return idx
            if hexc[idx:idx+2] == '2c':
                packed = hexc[idx+18:idx+20]
                packed = "{0:08b}".format(int(packed, 16))
                LCT = 0
                if packed[7] == '1':
                    N = int(packed[0:3], 2) + 1
                    LCT = pow(2, N)
                idx += 20 + (3 * LCT) + 2
                return idx

    if hexc[0:4] != '4749':
        return False
    if hexc[8:12] != '3961':
        return False

    packed = hexc[20:22]
    packed = "{0:08b}".format(int(packed, 16))
    GCT = 0
    if packed[0] == '1':
        N = int(packed[5:8],2) + 1
        GCT = pow(2, N)

    skip = (6*2)+(7*2)+(3*GCT)
    idx = skip

    while True:
        if hexc[idx:idx+2] == '2c':
            packed = hexc[idx+18:idx+20]
            packed = "{0:08b}".format(int(packed, 16))
            LCT = 0
            if packed[7] == '1':
                N = int(packed[0:3], 2) + 1
                LCT = pow(2, N)
            idx += 20 + (3 * LCT) + 2

        if hexc[idx:idx+2] == '3b':
            break
        elif hexc[idx:idx+2] == '21':
            idx = extension(idx)
        else:
            while hexc[idx:idx+2] != '00':
                s = int(hexc[idx:idx+2],16)
                idx += 2 + (s * 2)
            idx += 2

    if len(hexc) != idx + 2:
        return unsafe()
    else:
        return True
