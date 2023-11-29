def build_table(table, power=False):
    mod = len(table) + (1 if power else 0)
    str_len = len(str(mod)) + (1 if power else 0)
    rtn_str = ' ' * (str_len + 3)
    rtn_str += ' '.join(f'{" " * (str_len - len(str(a)))}{a}' for a in range(mod))
    rtn_str += f"\n{'-' * ((str_len + 1) * (mod + 1) + 1)}\n"
    i = 1 if power else 0
    for row in table:
        rtn_str += f'{" " * (str_len - len(str(i)))}{i} | '
        rtn_str += ' '.join(f'{" " * (str_len - 1 - len(str(row[a])))}*1'
                            if power and 1 in row[1:] and a == row[1:].index(1) + 1
                            else f'{" " * (str_len - len(str(row[a])))}{row[a]}'
                            for a in range(mod))
        rtn_str += '\n'
        i += 1
    return rtn_str


def add_table(mod):
    table = [[(a + b) % mod for a in range(mod)] for b in range(mod)]
    print(build_table(table))
    return table


def mul_table(mod):
    table = [[(a * b) % mod for a in range(mod)] for b in range(mod)]
    print(build_table(table))
    return table


def pow_table(mod):
    table = [[(b ** a) % mod for a in range(mod)] for b in range(1, mod)]
    print(build_table(table, power=True))
    return table


def get_generators(mod):
    table = []
    for b in range(1, mod):
        row = [(b ** a) % mod for a in range(mod)]
        if 1 in row[1:] and len(row) - 1 == row[1:].index(1) + 1:
            table.append(row)
            print(row)
        # table = [row for row in pow_table(mod) if 1 in row[1:] and len(row) - 1 == row[1:].index(1) + 1]
    return table


# get_generators(4969)
