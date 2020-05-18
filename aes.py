def roundcount(round):
    rc = { 1: 0x01, 2: 0x02, 3: 0x04, 4: 0x08, 5: 0x10, 6: 0x20, 7: 0x40, 8: 0x80, 9: 0x1B, 10: 0x36}
    return rc[round]

def xor_8(a,b):
    if(type(a) != bytearray or type(b) != bytearray): raise ValueError("types should be bytearray, they are ", type(a), type(b))
    if(len(a) != 1 or len(b) != 1): raise ValueError("sizes should be 1, they are",len(a), len(b))
    result = bytearray(1)
    result[0] = a[0] ^ b[0]
    return result

def xor_32(a, b):
    if(type(a) != bytearray or type(b) != bytearray): raise ValueError("types should be bytearray, they are ", type(a), type(b))
    if(len(a) != 4 or len(b) != 4): raise ValueError("sizes should be 4, they are",len(a), len(b))
    result = bytearray(4)
    for i in range(4):
        result[i] = a[i] ^ b[i]
    return result

def xor_128(a, b):
    if(type(a) != bytearray or type(b) != bytearray): raise ValueError("types should be bytearray, they are ", type(a), type(b))
    if(len(a) != 16 or len(b) != 16): raise ValueError("sizes should be 16, they are",len(a), len(b))
    result = bytearray(16)
    for i in range(16):
        result[i] = a[i] ^ b[i]
    return result

def two(in_byte):
    def setBit(int_type, offset, value):
        mask = value << offset
        return(int_type | mask)

    def testBit(int_type, offset):
        mask = 1 << offset
        return(int_type & mask)

    result = 0
    result = setBit(result, 7, int(testBit(in_byte, 6) != 0))
    result = setBit(result, 6, int(testBit(in_byte, 5) != 0))
    result = setBit(result, 5, int(testBit(in_byte, 4) != 0))
    result = setBit(result, 4, int(testBit(in_byte, 3) != 0) ^ int(testBit(in_byte, 7) != 0))

    result = setBit(result, 3, int(testBit(in_byte, 2) != 0) ^ int(testBit(in_byte, 7) != 0))
    result = setBit(result, 2, int(testBit(in_byte, 1) != 0))
    result = setBit(result, 1, int(testBit(in_byte, 0) != 0) ^ int(testBit(in_byte, 7) != 0))
    result = setBit(result, 0, int(testBit(in_byte, 7) != 0))
    return result

def three(in_byte):
    def setBit(int_type, offset, value):
        mask = value << offset
        return(int_type | mask)

    def testBit(int_type, offset):
        mask = 1 << offset
        return(int_type & mask)

    result = 0
    result = setBit(result, 7, int(testBit(in_byte, 7) != 0) ^ int(testBit(in_byte, 6) != 0))
    result = setBit(result, 6, int(testBit(in_byte, 6) != 0) ^ int(testBit(in_byte, 5) != 0))
    result = setBit(result, 5, int(testBit(in_byte, 5) != 0) ^ int(testBit(in_byte, 4) != 0))
    result = setBit(result, 4, int(testBit(in_byte, 4) != 0) ^ int(testBit(in_byte, 3) != 0) ^ int(testBit(in_byte, 7) != 0))

    result = setBit(result, 3, int(testBit(in_byte, 3) != 0) ^ int(testBit(in_byte, 2) != 0) ^ int(testBit(in_byte, 7) != 0))
    result = setBit(result, 2, int(testBit(in_byte, 2) != 0) ^ int(testBit(in_byte, 1) != 0))
    result = setBit(result, 1, int(testBit(in_byte, 1) != 0) ^ int(testBit(in_byte, 0) != 0) ^ int(testBit(in_byte, 7) != 0))
    result = setBit(result, 0, int(testBit(in_byte, 0) != 0) ^ int(testBit(in_byte, 7) != 0))
    return result

def key_addition(state, subkey):
    # direction is not yet implemented
    # types should be bytearray of size 16 (128-bit)
    if(type(state) != bytearray or type(subkey) != bytearray): raise ValueError("types should be bytearray, they are ", type(state), type(subkey))
    if(len(state) != 16 or len(subkey) != 16): raise ValueError("sizes should be 16, they are",len(state), len(subkey))
    result = xor_128(state, subkey)
    return result

def byte_substitution(direction, state):
    return sbox(direction, state)

def shift_rows(direction, state):
    # state should be a bytearray of size 16 (128-bit)
    if(direction == "forward"):
        result = bytearray(16)
        result[0] = state[0]
        result[1] = state[5]
        result[2] = state[10]
        result[3] = state[15]
        result[4] = state[4]
        result[5] = state[9]
        result[6] = state[14]
        result[7] = state[3]
        result[8] = state[8]
        result[9] = state[13]
        result[10] = state[2]
        result[11] = state[7]
        result[12] = state[12]
        result[13] = state[1]
        result[14] = state[6]
        result[15] = state[11]

        return result
    else:
        raise NotImplementedError



def mix_column(direction, state):
    # reverse direction is not yet implemented
    if(direction == "forward"):
        # one mixcolumn box
        out = bytearray(16)
        for i in range(4):
            out[i*4]   = two(state[i*4]) ^ three(state[i*4+1]) ^ state[i*4+2] ^ state[i*4+3]
            out[i*4+1] = state[i*4] ^ two(state[i*4+1]) ^ three(state[i*4+2]) ^ state[i*4+3]
            out[i*4+2] = state[i*4] ^ state[i*4+1] ^ two(state[i*4+2]) ^ three(state[i*4+3])
            out[i*4+3] = three(state[i*4]) ^ state[i*4+1] ^ state[i*4+2] ^ two(state[i*4+3])
        return out
    else:
        raise NotImplementedError

def g_function(word, counter):
    # gets 32 bits (byte array of 4), permutates with left shift, then s-box, then xor with RC
    permutated = bytearray(4)
    result = bytearray(4)
    boxed = bytearray(4)
    permutated[3] = word[0]
    for i in range(3):
        permutated[i] = word[i+1]
    boxed = sbox("forward", permutated)
    result[0] = xor_8(bytearray([boxed[0]]), bytearray([counter]))[0]
    for i in range(3):
        result[i+1] = boxed[i+1]
    return result

def h_function(word):
    result = bytearray(4)
    result = sbox("forward", word)
    return result

def generate_subkeys(mode, main_key):
    # generates subkeys from main key, returns list of round keys (either 10, 12 or 14)
    # all round keys are byte arrays of size 16 (128 bit)
    # all words are byte arrays of size 4 (32 bit)
    if(mode == 128):
        keys = []
        words = []
        for i in range(4):
            # set first words based on main key
            words.append( bytearray( [main_key[i*4], main_key[(i*4)+1], main_key[(i*4)+2], main_key[(i*4)+3]] ) )
        
        # append the first words to result key
        keys.append(bytearray( words[0] + words[1] + words[2] + words[3] ))
        
        # calculate round keys
        for i in range(10):
            words.append( xor_32(words[i*4], g_function(words[i*4+3], roundcount(i+1))) )
            words.append( xor_32(words[i*4+4], words[i*4+1]) )
            words.append( xor_32(words[i*4+5], words[i*4+2]) )
            words.append( xor_32(words[i*4+6], words[i*4+3]) )
            keys.append(bytearray( words[i*4+4] + words[i*4+5] + words[i*4+6] + words[i*4+7] ))
        return keys
    elif(mode == 192):
        keys = []
        words = []
        for i in range(6):
            # set words based on main key
            words.append( bytearray( [main_key[i*4], main_key[(i*4)+1], main_key[(i*4)+2], main_key[(i*4)+3]] ) )
        # main key is first round key
        # keys.append(bytearray( words[0] + words[1] + words[2] + words[3] + words[4] + words[5] ))
        # calculate round keys
        for i in range(8):
            words.append( xor_32(words[i*6], g_function(words[i*6+5], roundcount(i+1))) )
            words.append( xor_32(words[i*6+ 6], words[i*6+1]) )
            words.append( xor_32(words[i*6+ 7], words[i*6+2]) )
            words.append( xor_32(words[i*6+ 8], words[i*6+3]) )
            words.append( xor_32(words[i*6+ 9], words[i*6+4]) )
            words.append( xor_32(words[i*6+10], words[i*6+5]) )

        for i in range(13):
            keys.append(bytearray( words[i*4] + words[i*4+1] + words[i*4+2] + words[i*4+3] ))
        return keys
    elif(mode == 256):
        keys = []
        words = []
        for i in range(8):
            # set words based on main key
            words.append( bytearray( [main_key[i*4], main_key[(i*4)+1], main_key[(i*4)+2], main_key[(i*4)+3]] ) )
        # main key is first round key
        # keys.append(bytearray( words[0] + words[1] + words[2] + words[3] + words[4] + words[5] ))
        # calculate round keys
        for i in range(7):
            words.append( xor_32(words[i*8], g_function(words[i*8+7], roundcount(i+1))) )
            words.append( xor_32(words[i*8+ 8], words[i*8+1]) )
            words.append( xor_32(words[i*8+ 9], words[i*8+2]) )
            words.append( xor_32(words[i*8+10], words[i*8+3]) )

            words.append( xor_32( h_function(words[i*8+11]), words[i*8+4]) )
            words.append( xor_32(words[i*8+12], words[i*8+5]) )
            words.append( xor_32(words[i*8+13], words[i*8+6]) )
            words.append( xor_32(words[i*8+14], words[i*8+7]) )

        for i in range(15):
            keys.append(bytearray( words[i*4] + words[i*4+1] + words[i*4+2] + words[i*4+3] ))
        return keys
    else:
        raise ValueError("this is not good")

def sbox(direction, input):
    # input is a byte array
    result = bytearray(len(input))
    rijndael_sbox = (
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
    )
    rijndael_inv_sbox = (
        0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
        0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
        0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
        0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
        0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
        0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
        0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
        0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
        0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
        0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
        0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
        0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
        0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
        0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
        0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
    )
    if(direction == "forward"):
        for i in range(len(input)):
            result[i] = rijndael_sbox[input[i]]
        return result
    elif(direction == "reverse"):
        for i in range(len(input)):
            result[i] = rijndael_sbox[input[i]]
        return result
    else:
        raise ValueError




def encrypt(mode, plaintext, masterkey):
    # plaintext should be 16 byte bytearray
    # depending on mode, determine amount of rounds
    # AES-128: 10 rounds
    # AES-192: 12 rounds
    # AES-256: 14 rounds
    modeDict = {128: 10, 192: 12, 256: 14}
    state = bytearray(16)
    # generate subkeys, save into key array
    keys = generate_subkeys(mode, masterkey)
    if(verbose):
        print("Plaintext:")
        print(str(''.join(format(x, '02x') for x in ( plaintext ))), "\n")
        print("Main key:")
        print(str(''.join(format(x, '02x') for x in ( masterkey ))), "\n")
        print("Derived keys:")
        for i in range(modeDict[mode]+1):
            print(str(''.join(format(x, '02x') for x in ( generate_subkeys(mode, masterkey)[i] ))))

    #key addition before rounds start
    if(verbose): print("\nFirst round: Key addition")
    state = key_addition(plaintext, keys[0])
    if(verbose): print("current state is", str(''.join(format(x, '02x') for x in ( state ))), "\n")

    #rounds start
    for i in range(modeDict[mode]):
        if(verbose): print("round", i+1, "starting")

        #  Byte substitution
        if(verbose): print("substituting bytes")
        state = byte_substitution("forward", state)
        if(verbose): print("current state is", str(''.join(format(x, '02x') for x in ( state ))))
        
        # shift rows
        if(verbose): print("shifting rows")
        state = shift_rows("forward", state)
        if(verbose): print("current state is", str(''.join(format(x, '02x') for x in ( state ))))
        
        if(i < modeDict[mode]-1):
            # mix column
            if(verbose): print("mixing columns")
            state = mix_column("forward", state)
            if(verbose): print("current state is", str(''.join(format(x, '02x') for x in ( state ))))

        # key addition
        if(verbose): print("adding subkey", str(''.join(format(x, '02x') for x in ( keys[i+1] ))))
        state = key_addition(state, keys[i+1])
        if(verbose): print("current state is", str(''.join(format(x, '02x') for x in ( state ))))
        if(verbose): print("round", i+1, "complete.\n\n")
    return state

def decrypt(mode):
    # TODO: decryption function
    print("decryption function; not yet implemented")

verbose = 1

key  = bytearray(b"\x54\x68\x61\x74\x73\x20\x6d\x79\x20\x4b\x75\x6e\x67\x20\x46\x75")

crypto_key = bytearray("Einfuehrung in die Kryptographie", "ascii")

plaintext1 = bytearray(b"\x00\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
plaintext2 = bytearray(b"\x00\x00\x00\x00\x00\x22\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

print("encrypting plaintext1")
print(str(''.join(format(x, '02x') for x in ( encrypt(128, plaintext1, key) ))))

print("encrypting plaintext2")
print(str(''.join(format(x, '02x') for x in ( encrypt(128, plaintext2, key) ))))

print("Key schedule example")
print("Main key:")
print(str(''.join(format(x, '02x') for x in ( crypto_key ))), "\n")
print("Main key length:", len(crypto_key)*8, "bits")
print("Derived keys:")
for i in range(15):
    print(str(''.join(format(x, '02x') for x in ( generate_subkeys(256, crypto_key)[i] ))))