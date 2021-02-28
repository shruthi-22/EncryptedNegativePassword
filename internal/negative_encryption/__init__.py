from internal.helpers import create_sequence_of_symbols, to_symbol, invert_bits, number_of_SP, index_of_SP
from internal.constants import pi, pi_inv


def permute(bin_string):
    permuted_string = [0] * 256

    idx = 0
    for position in pi:
        permuted_string[idx] = bin_string[position - 1]
        idx += 1
    return ''.join(permuted_string)


def inverse_permutation(bin_string):
    permuted_string = [0] * 256

    idx = 0
    for position in pi_inv:
        permuted_string[idx] = bin_string[position - 1]
        idx += 1
    return ''.join(permuted_string)


def negative_password(hashed_binary):
    ndb = []
    permuted_bits = permute(hashed_binary)
    m = len(permuted_bits)
    for i in range(m):
        x = create_sequence_of_symbols(m)
        for j in range(i):
            x[j] = to_symbol(permuted_bits[j])
        x[i] = to_symbol(invert_bits(permuted_bits[i]))
        for j in range(i + 1, m):
            x[j] = '*'
        x = ''.join(x)
        ndb.append(inverse_permutation(x))
    return ndb


def enp_verify(hashP, np):
    m = len(hashP)
    x = ['0'] * m
    for i in range(m):
        if number_of_SP(np[i]) != i + 1:
            return False

    for i in range(m):
        if number_of_SP(np[i]) != 1:
            return False
        k = index_of_SP(np[i])
        x[k] = '1' if np[i][k] == '0' else '0'
        for j in range(i + 1, m):
            if np[j][k] != x[k]:
                return False
            np[j] = np[j][:k] + '*' + np[j][k + 1:]
    x = "".join(x)

    if x == hashP:
        return True
    else:
        return False
