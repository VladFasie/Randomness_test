

# extrage bitul de pe pozitia p
# msb are pozitia 0
def bit(n, p):
    return (n >> (31 - p)) & 1

def intToStrBin(n, len):
    r = ''
    for i in range(32):
        r += str(bit(n, i))
    return r[32 - len:]

def count_all(string, substring):
    results = 0
    sub_len = len(substring)
    for i in range(len(string)):
        if string[i:i + sub_len] == substring:
            results += 1
    return results