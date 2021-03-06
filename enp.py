import hashlib

def hash(plaintext):
    return hashlib.sha256(plaintext.encode())

def perfect_hex(bin_string):
    l = len(bin_string)
    k = 4 - l
    hex_string = str(0*k) + bin_string
    return hex_string

def permute(bin_string):

    pi = [201, 237, 97, 67, 172, 140, 9, 190, 36, 187,
135, 178, 216, 222, 167, 230, 169, 49, 66, 214, 175, 98, 113,
34, 93, 11, 43, 111, 23, 40, 250, 63, 130, 215, 94, 90, 176,
37, 38, 83, 27, 7, 141, 99, 10, 177, 107, 131, 217, 101, 120,
254, 32, 242, 115, 174, 233, 58, 157, 15, 194, 46, 184, 253,
200, 168, 236, 148, 104, 2, 17, 124, 20, 202, 80, 6, 70, 192,
208, 118, 180, 226, 211, 203, 225, 209, 29, 65, 136, 228, 51,
8, 235, 96, 227, 60, 181, 26, 72, 129, 126, 77, 188, 127, 198,
210, 159, 1, 74, 3, 185, 103, 170, 114, 47, 244, 64, 78, 18,
25, 162, 155, 109, 76, 116, 164, 12, 108, 232, 246, 87, 21,
154, 161, 240, 42, 59, 134, 35, 142, 95, 143, 173, 71, 179,
88, 229, 147, 41, 238, 61, 158, 146, 138, 196, 212, 204, 197,
241, 182, 85, 30, 55, 186, 234, 91, 52, 13, 73, 28, 199, 218,
206, 163, 205, 56, 213, 39, 221, 82, 4, 224, 156, 193, 256,
248, 62, 219, 165, 48, 151, 54, 149, 231, 239, 132, 195, 102,
125, 75, 92, 57, 128, 105, 44, 69, 220, 19, 14, 112, 86, 255,
33, 166, 79, 53, 31, 24, 84, 100, 223, 117, 122, 5, 160, 153,
45, 191, 183, 121, 245, 207, 145, 133, 189, 123, 247, 50, 251,
144, 139, 68, 110, 81, 252, 137, 249, 171, 152, 106, 243, 119,
22, 150, 16, 89]

    permuted_string = [0]*256

    idx = 0
    for position in pi:
        permuted_string[idx] = bin_string[position-1]
        idx += 1
    return ''.join(permuted_string)

def inverse_permutation(bin_string):

    pi_inv = [108, 70, 110, 181, 224, 76, 42, 92, 7, 45, 26, 127,
     168, 209, 60, 255, 71, 119, 208, 73, 132, 253, 29, 218, 120, 
     98, 41, 170, 87, 162, 217, 53, 213, 24, 139, 9, 38, 39, 178, 
     30, 149, 136, 27, 205, 227, 62, 115, 190, 18, 238, 91, 167, 
     216, 192, 163, 176, 202, 58, 137, 96, 151, 187, 32, 117, 88, 
     19, 4, 242, 206, 77, 144, 99, 169, 109, 200, 124, 102, 118, 
     215, 75, 244, 180, 40, 219, 161, 211, 131, 146, 256, 36, 166,
    201, 25, 35, 141, 94, 3, 22, 44, 220, 50, 198, 112, 69, 204,
    250, 47, 128, 123, 243, 28, 210, 23, 114, 55, 125, 222, 80,
    252, 51, 230, 223, 236, 72, 199, 101, 104, 203, 100, 33,
    48, 196, 234, 138, 11, 89, 246, 154, 241, 6, 43, 140, 142,
    240, 233, 153, 148, 68, 193, 254, 191, 249, 226, 133, 122, 
    183, 59, 152, 107, 225, 134, 121, 174, 126, 189, 214, 15, 66, 
    17, 113, 248, 5, 143, 56, 21, 37, 46, 12, 145, 81, 97, 160, 229, 
    63, 111, 164, 10, 103, 235, 8, 228, 78, 184, 61, 197, 155, 158, 105, 
    171, 65, 1, 74, 84, 157, 175, 173, 232, 79, 86, 106, 83, 156, 177, 20, 
    34, 13, 49, 172, 188, 207, 179, 14, 221, 182, 85, 82, 95, 90, 147, 16, 194, 
    129, 57, 165, 93, 67, 2, 150, 195, 135, 159, 54, 251, 116, 231, 130, 237, 
    186, 247, 31, 239, 245, 64, 52, 212, 185]

    permuted_string = [0]*256

    idx = 0
    for position in pi_inv:
        permuted_string[idx] = bin_string[position-1]
        idx += 1
    return ''.join(permuted_string)

def invert_bits(bin_string):

    inverted_string = [0]*len(bin_string)
    idx = 0
    for bit in bin_string:
        if bit == '0':
            inverted_string[idx] = '1'
        else:
            inverted_string[idx] = '0'
    return ''.join(inverted_string)

 
def create_sequence_of_symbols(m):
    return ['*'] * m    

def toSymbol(bit):
    if bit == '0':
        return '0'
    else:
        return '1'


def negative_password(hashed_binary):

    ndb = []
    permuted_bits = permute(hashed_binary)

    print('\nPassword after pi :', permuted_bits)
    m = len(permuted_bits)
    for i in range(m): 
        x = create_sequence_of_symbols(m)       
        for j in range(i):
            x[j] = toSymbol(permuted_bits[j])       
        x[i] = toSymbol(invert_bits(permuted_bits[i]))
        for j in range(i+1,m):   
            x[j] = '*'
        x = ''.join(x)
        ndb.append(inverse_permutation(x))
    return ndb
    

if __name__ == "__main__":

    plaintext = 'password'
    print("\nPlaintext : ", plaintext)

    hashed_text_hex = hash(plaintext).hexdigest()
    print("\nHashed Text : ", hashed_text_hex)

    hashed_text_bin = bin(int(hashed_text_hex, 16))[2:]
    hashed_text_bin = perfect_hex(hashed_text_bin)
    print("\nhashed Text binary : ",hashed_text_bin)

    negative = negative_password(hashed_text_bin)
    #encrypted_negative_passwd = aes(negative,)


