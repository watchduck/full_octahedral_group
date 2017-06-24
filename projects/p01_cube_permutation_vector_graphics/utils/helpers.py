import numpy as np
from itertools import permutations
from math import factorial


def binary_str_to_list(s):
    # gives [False, True] for input '01'
    return [bool(int(d)) for d in s]


def number_to_reverse_binary_string(n, length):
    return "{0:b}".format(n).zfill(length)[::-1]


def number_to_reverse_binary_list(n, length):
    return binary_str_to_list(number_to_reverse_binary_string(n, length))


def ordered_perms(elements):
    n = len(elements)
    perms_mat = np.zeros([factorial(n), n], dtype=int)
    perms_iter = permutations(elements)
    for i, perm in enumerate(perms_iter):
        perms_mat[i, :] = perm
    return np.fliplr(np.flipud(perms_mat))


def concat(p1, p2):  # p1 after p2  (left action)
    return [p1[i] for i in p2]
