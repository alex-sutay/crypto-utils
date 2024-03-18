

def ssp(s, t):
    vs = []
    for i in range(2**len(s)):
        st = bin(i)[2:].rjust(len(s), '0')
        if sum(s[j] for j in range(len(s)) if st[j] == '1') == t:
            vs.append([int(j) for j in st])
    return vs


print(ssp([1033, 7365, 1999, 2376, 5439, 2871, 5555, 9323, 6210, 4877], 24269))

print(ssp([3, 7, 19, 43, 89, 195], 260))
print(ssp([5, 11, 25, 61, 125, 261], 408))
print(ssp([2, 5, 12, 28, 60, 131, 257], 340))
print(ssp([4, 12, 15, 36, 75, 162], 214))

