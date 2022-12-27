import numpy as np


def decrypt(cipher):
    dec_list = [[] for i in range(7)]
    others = []
    for i in range(len(cipher)):
        if not cipher[i] in dec_alph:
            others.append(cipher[i])
        else:
            others.append('-1')
    c = 0
    for i in range(len(cipher)):
        if others[i] == '-1':
            dec_list[(i-c) % 7].append(cipher[i])
        else:
            c += 1
    temp_key = [x for x in key]
    for i in range(len(temp_key)):
        mn = [temp_key[i], i]
        for j in range(i, len(temp_key)):
            if mn[0] > temp_key[j]:
                mn[0], mn[1] = key[j], j
        temp_key[i], temp_key[mn[1]] = temp_key[mn[1]], temp_key[i]



    sad = min([len(h) for h in dec_list])
    counts = sum([1 for x in dec_list if len(x) > sad])
    swap_order = [temp_key.index(x) for x in key]

    temp_order = [z for z in swap_order if z >= counts]
    if counts != 0 and counts != len(temp_key):
        cnt = 0
        for i in range(counts):
            if len(dec_list[i]) != sad and swap_order.index(i) < counts:
                cnt += 1
            elif len(dec_list[temp_order[i]]) == sad:
                dec_list[temp_order[i - cnt]].append(dec_list[i][-1])
                dec_list[i].pop(-1)
    for i in range(len(key)):
        ind = temp_key.index(key[i])
        dec_list[i], dec_list[ind] = dec_list[ind], dec_list[i]
        temp_key[i], temp_key[ind] = temp_key[ind], temp_key[i]

    temp_res = ""
    c = 0
    for i in range(len(cipher)):
        if others[i] == '-1':
            temp_res += dec_list[(i-c) % 7][(i-c) // 7]
        else:
            c += 1
    res = ""
    c = 0
    while c != len(others):
        if others[c] == '-1':
            res += X[dec_alph[temp_res[c]]][dec_alph[temp_res[c + 1]]]
            c += 2
        else:
            res += others[c]
            others.pop(c)
    return res

def encrypt(message):
    temp = ""
    temp_list = []
    others = []
    for i in range(len(message)):
        if message[i] in alphas:
            col = int(alphas[message[i]].split()[1])
            row = int(alphas[message[i]].split()[0])
            temp += f"{ciph_alph[row]}{ciph_alph[col]}"
            others.append('-1')
            others.append('-1')
        else:
            others.append(message[i])
    for i in range(len(key)):
        temp_list.append([temp[x] for x in range(len(temp)) if (x % len(key) + 1) == (i + 1)])
    temp_key = [x for x in key]
    for i in range(len(temp_key)):
        mn = [temp_key[i], i]
        for j in range(i, len(temp_key)):
            if mn[0] > temp_key[j]:
                mn[0], mn[1] = key[j], j
        temp_key[i], temp_key[mn[1]] = temp_key[mn[1]], temp_key[i]
        temp_list[i], temp_list[mn[1]] = temp_list[mn[1]], temp_list[i]


    temp_swap_order = list(map(int, "0 1 5 4 3 6 2".split()))
    sad = min([len(h) for h in temp_list])
    counts = sum([1 for x in temp_list if len(x) > sad])
    swap_order = [temp_key.index(x) for x in key]
    temp2 = [z for z in swap_order if z >= counts]
    if counts != 0 and counts != len(temp_key):
        cnt = 0
        for i in range(counts):
            if len(temp_list[i]) == sad:
                temp_list[i].append(temp_list[temp2[i - cnt]][-1])
                temp_list[temp2[i - cnt]].pop(-1)
            else:
                cnt += 1
    res = ""
    c = 0
    for i in range(len(others)):
        if others[i] != '-1':
            res += others[i]
            others[i] = '-1'
            c += 1
        else:
            res += f"{temp_list[(i-c) % 7][(i-c) // 7]}"
    return res
ciph_alph = {0: 'A', 1: 'D', 2: 'F', 3: 'G', 4: 'X'}
dec_alph = {'A': 0, 'D': 1, 'F': 2, 'G': 3, 'X': 4}
key = "formula"
alphas = {"y": "0 0", "o": "0 1", "l": "0 2", "r": "0 3", "z": "0 4",
          "w": "1 0", "b": "1 1", "d": "1 2", "u": "1 3", "f": "1 4",
          "x": "2 0", "n": "2 1", "v": "2 2", "s": "2 3", "t": "2 4",
          "c": "3 0", "m": "3 1", "q": "3 2", "e": "3 3", "a": "3 4",
          "k": "4 0", "i": "4 1", "j": "4 1", "h": "4 2", "p": "4 3", "g": "4 4"}
X = np.array([["y", "o", "l", "r", "z"],
              ["w", "b", "d", "u", "f"],
              ["x", "n", "v", "s", "t"],
              ["c", "m", "q", "e", "a"],
              ["k", "i", "h", "p", "g"]])
