

def xor(it):
    return sum(it) % 2


def lfsr(prefixes, iv):
    seen = set()
    curr = iv
    rtnlist = [curr]
    while curr not in seen:
        seen.add(curr)
        new = ''.join(curr[i] for i in range(len(curr) - 1))
        new = str(xor(int(curr[::-1][i]) for i in prefixes)) + new
        curr = new
        rtnlist.append(curr)
    return rtnlist


m = 9
out = lfsr([0, 1], '1' * m)
print(*(o for o in out), sep='\n')
print(len(out), len(out) == 2**m)
