import hashlib


def hash_plain_text(plaintext):
    return hashlib.sha256(plaintext.encode())


def perfect_hex(bin_string):
    l = len(bin_string)
    k = 256 - l
    hex_string = '0' * k + bin_string
    return hex_string


def invert_bits(bin_string):
    inverted_string = [0] * len(bin_string)
    idx = 0
    for bit in bin_string:
        if bit == '0':
            inverted_string[idx] = '1'
        else:
            inverted_string[idx] = '0'
    return ''.join(inverted_string)


def create_sequence_of_symbols(m):
    return ['*'] * m


def to_symbol(bit):
    if bit == '0':
        return '0'
    else:
        return '1'


def number_of_SP(text):
    return len(text) - text.count('*')


def index_of_SP(text):
    if '1' in text:
        return text.index('1')
    else:
        return text.index('0')


def write_to_a_file(name, content_list):
    f = open(name, "a")
    for i in content_list:
        t = str(i)[2:-1]
        f.write(t + "\n")
    f.close()


def read_from_file(name):
    f = open(name, "r")
    arr_list = []
    for x in f:
        arr_list.append(x)
    return arr_list


def render_html(text):
    return "<html><style></style><body><h1>" + text + "</h1></body></html>"


def get_hashed_text_binary(plain_text):
    hashed_text_hex = hash_plain_text(plain_text).hexdigest()
    hashed_text_bin = bin(int(hashed_text_hex, 16))[2:]
    hashed_text_bin = perfect_hex(hashed_text_bin)
    return hashed_text_bin


def is_file_exists(fname):
    import os.path
    return os.path.isfile(fname)
