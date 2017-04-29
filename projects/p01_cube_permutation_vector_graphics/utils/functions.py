from math import sqrt
import numpy as np

from .constants import cc
from .helpers import ordered_perms, number_to_reverse_binary_list, concat


ordered_perms_of_1247 = ordered_perms([1, 2, 4, 7])  # permutations of 1, 2, 4, 7 in reverse colexicographic order


def perm8_to_perm4_id(perm8, perm_is_inversion):
    perm8_inv = inverse_permutation(perm8)
    if not perm_is_inversion:
        perm4_to_be_found = [perm8_inv[i] for i in [1, 2, 4, 7]]
    else:
        perm4_to_be_found = [perm8_inv[i] for i in [6, 5, 3, 0]]
    perms4 = ordered_perms_of_1247
    for i in range(24):
        perm4_inv = inverse_permutation(perms4[i], [1, 2, 4, 7])
        if perm4_to_be_found == perm4_inv:
            return i


ordered_perms_of_012 = ordered_perms([0, 1, 2])  # permutations of 0, 1, 2 in reverse colexicographic order

letters = ['A', 'B', 'C']

bit_patterns = [
    np.array([0, 1, 0, 1, 0, 1, 0, 1], dtype=bool),
    np.array([0, 0, 1, 1, 0, 0, 1, 1], dtype=bool),
    np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype=bool)
]


def position_to_permutation_properties(row, col):

    # 3x3 matrix of the linear transformation
    # a.k.a. signed permutation matrix
    perm_of_012 = ordered_perms_of_012[col]
    signed_permutation_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for k in range(3):
        v = perm_of_012[k]
        signed_permutation_matrix[v][k] = 1
    horizontal_negator_pattern = number_to_reverse_binary_list(row, 3)
    for i in range(3):
        for j in range(3):
            if horizontal_negator_pattern[i]:
                signed_permutation_matrix[i][j] *= -1
    determinant = np.linalg.det(signed_permutation_matrix)

    # letters and their negators
    # binary 3x8 matrix: rows correspond to those of 3x3 matrix, cols to elements of permutation
    letter_pattern = []
    letter_negator_pattern = []
    horizontal_matrix = np.zeros([3, 8], dtype=bool)
    for i in range(3):
        for j in range(3):
            entry = signed_permutation_matrix[i][j]
            if entry != 0:
                letter_pattern.append(letters[j])
                if entry == 1:
                    letter_negator_pattern.append(False)
                    horizontal_matrix_row = bit_patterns[j]
                elif entry == -1:
                    letter_negator_pattern.append(True)
                    horizontal_matrix_row = np.bitwise_not(bit_patterns[j])
                horizontal_matrix[i, 0:8] = horizontal_matrix_row

    # permutation of 8 elements
    powers_of_two = np.array([1, 2, 4])
    perm = list(np.dot(powers_of_two, horizontal_matrix))

    perm_is_inversion = False if row in [0, 3, 5, 6] else True
    col_is_odd = False if col in [0, 3, 4] else True

    # determine S4 based identifiers and corresponding colors
    perm_id_num = perm8_to_perm4_id(perm, perm_is_inversion)  # numerical part of the S4 based identifier
    perm_id = str(perm_id_num) if not perm_is_inversion else str(perm_id_num)+"'"  # add apostrophe if perm_is_inversion

    green_or_blue_perm_nums = [1, 2, 5, 6, 14, 21]
    orange_or_red_perm_nums = [9, 10, 13, 17, 18, 22]
    bold_perm_nums = [0, 7, 16, 23]

    if perm_id_num in green_or_blue_perm_nums:
        perm_id_color = 'green' if not perm_is_inversion else 'blue'
    elif perm_id_num in orange_or_red_perm_nums:
        perm_id_color = 'orange' if not perm_is_inversion else 'red'
    else:
        perm_id_color = 'white' if not perm_is_inversion else 'yellow'

    perm_id_bold = False
    if perm_id_num in bold_perm_nums:
        perm_id_bold = True

    # set partition colors
    set_partition_colors = calculate_set_partition_colors(perm, perm_id, perm_id_color, perm_id_bold)

    return {
        'row': row,
        'col': col,
        'signed_perm_mat': signed_permutation_matrix,
        'horz_mat': horizontal_matrix,
        'perm': perm,
        'id': perm_id,
        'id_num': perm_id_num,
        'id_color': perm_id_color,
        'id_bold': perm_id_bold,
        'perm_is_inversion': perm_is_inversion,
        'col_is_odd': col_is_odd,
        'determinant': determinant,
        'letter_perm': letter_pattern,
        'negator_pattern': letter_negator_pattern,
        'inverse_perm': inverse_permutation(perm),
        'partition_colors': set_partition_colors
    }


def svg_path_for_arrow_in_permutation_matrix(a, b):
    p1 = '{a} {a}'.format(a=a)
    p3 = '{a} {b}'.format(a=a, b=b)
    if a < b:
        p2 = '{a} {b_}.5'.format(a=a, b_=b-1)
        p4 = '{a}.5 {b}'.format(a=a, b=b)
        p5 = '{b_}.62 {b}'.format(b_=b-1, b=b)
    elif a > b:
        p2 = '{a} {b}.5'.format(a=a, b=b)
        p4 = '{a_}.5 {b}'.format(a_=a-1, b=b)
        p5 = '{b}.38 {b}'.format(b=b)
    return 'M {p1}  L {p2}  C {p2}, {p3}, {p4}  L {p5}'.format(p1=p1, p2=p2, p3=p3, p4=p4, p5=p5)


def permutation_to_cycles(perm):
    to_be_checked = set(range(8))
    for k, v in enumerate(perm):
        if k == v:
            to_be_checked -= {k}  # remove fixed point from set
    cycles = []
    while to_be_checked:  # while set is not empty
        start = list(to_be_checked)[0]
        p = start
        cycle = []
        while True:
            cycle.append(p)
            to_be_checked -= {p}
            p = perm[p]
            if p == start:
                break
        cycles.append(cycle)
    return cycles


def calculate_set_partition_colors(perm, id, id_color, id_bold):

    set_part_colors = ['']*8

    for k, v in enumerate(perm):
        if k == v:
            set_part_colors[k] = 'black'

    if id == '0':
        pass
    elif id == "0'":
        set_part_colors = [cc['maindiag']]*8
    elif id_color == 'yellow' and id_bold:
        for i in range(8):
            set_part_colors[i] = cc['axis']
    elif id_color == 'yellow' and not id_bold:
        cycles = permutation_to_cycles(perm)
        for cycle in cycles:
            color = cc['bigcyc'] if len(cycle) == 6 else cc['maindiag']
            for c in cycle:
                set_part_colors[c] = color
    elif id_color == 'blue':
        for i in range(8):
            if i+perm[i] == 7:
                set_part_colors[i] = cc['maindiag']
        for i in range(8):
            if set_part_colors[i] == '':
                set_part_colors[i] = cc['axis']
    elif id_color == 'red':
        cycles = permutation_to_cycles(perm)
        for cycle in cycles:
            contains_zero = False
            for c in cycle:
                if c==0:
                    contains_zero = True
            color = cc['with0'] if contains_zero else cc['without0']  # the cycle including the zero has color c1, the other c2
            for c in cycle:
                set_part_colors[c] = color
    else:  # if row is even
        for i in range(8):
            if perm[i] != i:
                dark = i in [1, 2, 4, 7]
                set_part_colors[i] = cc['darktetra'] if dark else cc['lighttetra']

    return set_part_colors


def shorten_arrow(c1, c2, shorten_by, bidirectional):
    """``c1`` and ``c2`` are coordinate pairs of an arrow's start and end points.
    The arrow is to be shortened by the length of the arrow head."""
    (x1, y1) = c1
    (x2, y2) = c2
    (dx, dy) = (x2-x1, y2-y1)
    d_len = sqrt(dx**2 + dy**2)
    factor = shorten_by / d_len
    apply_x = dx * factor
    apply_y = dy * factor
    if not bidirectional:
        c1_new = c1
    else:
        x1_new = round(x1 + apply_x, 3)
        y1_new = round(y1 + apply_y, 3)
        c1_new = (x1_new, y1_new)
    x2_new = round(x2 - apply_x, 3)
    y2_new = round(y2 - apply_y, 3)
    c2_new = (x2_new, y2_new)
    return c1_new, c2_new


def inverse_permutation(perm, nonincreasing_identity=None):
    length = len(perm)
    if len(list(set(perm))) != length:
        print('No permutation was entered.')
    else:
        sorted_perm = sorted(perm)
        if not nonincreasing_identity:
            if sorted_perm == list(range(length)):  # if ``perm`` is a permutation of a range of integers starting with 0
                inverse = [0] * length
                for k, v in enumerate(perm):
                    inverse[v] = k
                return inverse
            else:
                natural_perm = []
                for p in perm:
                    for i, sp in enumerate(sorted_perm):
                        if sp == p:
                            natural_perm.append(i)
                inverse_of_natural_perm = inverse_permutation(natural_perm)
                return [sorted_perm[i] for i in inverse_of_natural_perm]
        else:
            decent_perm = []
            for p in perm:
                for nik, niv in enumerate(nonincreasing_identity):
                    if p == niv:
                        decent_perm.append(nik)
            decent_inv = inverse_permutation(decent_perm)
            actual_inv = []
            for i in range(length):
                actual_inv.append(
                    nonincreasing_identity[decent_inv[i]]
                )
            return actual_inv
