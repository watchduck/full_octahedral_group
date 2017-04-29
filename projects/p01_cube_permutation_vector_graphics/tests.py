from utils.functions import position_to_permutation_properties
from utils.helpers import ordered_perms, concat

from itertools import product
import numpy as np


# Create the Cayley table of S4 and that of the cube permutations.
# Check if the latter repeats the pattern of the former.

perms4 = ordered_perms(range(4))

cayley4 = np.zeros([24, 24], dtype=int)
for i in range(24):
    for j in range(24):
        result = concat(perms4[i], perms4[j])
        for k in range(24):
            if (perms4[k] == result).all():
                cayley4[i, j] = k

perms8 = [0]*48
for row in range(8):
    for col in range(6):
        perm_props = position_to_permutation_properties(row, col)
        perm = perm_props['perm']
        num = perm_props['id_num'] if not perm_props['perm_is_inversion'] else perm_props['id_num']+24
        perms8[num] = perm

cayley8 = np.zeros([48, 48], dtype=int)
for i in range(48):
    for j in range(48):
        result = concat(perms8[i], perms8[j])
        for k in range(48):
            if perms8[k] == result:
                cayley8[i, j] = k

tl_ok = np.array_equal(cayley8[0:24, 0:24], cayley4)
tr_ok = np.array_equal(cayley8[0:24, 24:48] - 24, cayley4)
bl_ok = np.array_equal(cayley8[24:48, 0:24] - 24, cayley4)
br_ok = np.array_equal(cayley8[24:48, 24:48], cayley4)

if tl_ok and tr_ok and bl_ok and br_ok:
    print('The Cayley table of cube rotations repeats the pattern of the Cayley table of S4.')


# Create Cayley table of 3x3 matrices and compare it to cayley8 created above.

lin_transform_matrices = {(7, 3): [[0, -1, 0], [0, 0, -1], [-1, 0, 0]], (1, 3): [[0, -1, 0], [0, 0, 1], [1, 0, 0]], (3, 0): [[-1, 0, 0], [0, -1, 0], [0, 0, 1]], (5, 4): [[0, 0, -1], [1, 0, 0], [0, -1, 0]], (2, 1): [[0, 1, 0], [-1, 0, 0], [0, 0, 1]], (6, 2): [[1, 0, 0], [0, 0, -1], [0, -1, 0]], (5, 1): [[0, -1, 0], [1, 0, 0], [0, 0, -1]], (2, 5): [[0, 0, 1], [0, -1, 0], [1, 0, 0]], (0, 3): [[0, 1, 0], [0, 0, 1], [1, 0, 0]], (7, 2): [[-1, 0, 0], [0, 0, -1], [0, -1, 0]], (4, 0): [[1, 0, 0], [0, 1, 0], [0, 0, -1]], (1, 2): [[-1, 0, 0], [0, 0, 1], [0, 1, 0]], (5, 5): [[0, 0, -1], [0, 1, 0], [-1, 0, 0]], (4, 4): [[0, 0, 1], [1, 0, 0], [0, -1, 0]], (6, 3): [[0, 1, 0], [0, 0, -1], [-1, 0, 0]], (1, 5): [[0, 0, -1], [0, 1, 0], [1, 0, 0]], (5, 0): [[-1, 0, 0], [0, 1, 0], [0, 0, -1]], (0, 4): [[0, 0, 1], [1, 0, 0], [0, 1, 0]], (3, 3): [[0, -1, 0], [0, 0, -1], [1, 0, 0]], (5, 3): [[0, -1, 0], [0, 0, 1], [-1, 0, 0]], (4, 1): [[0, 1, 0], [1, 0, 0], [0, 0, -1]], (1, 1): [[0, -1, 0], [1, 0, 0], [0, 0, 1]], (6, 4): [[0, 0, 1], [-1, 0, 0], [0, -1, 0]], (3, 2): [[-1, 0, 0], [0, 0, -1], [0, 1, 0]], (0, 0): [[1, 0, 0], [0, 1, 0], [0, 0, 1]], (7, 1): [[0, -1, 0], [-1, 0, 0], [0, 0, -1]], (4, 5): [[0, 0, 1], [0, 1, 0], [-1, 0, 0]], (2, 2): [[1, 0, 0], [0, 0, -1], [0, 1, 0]], (6, 0): [[1, 0, 0], [0, -1, 0], [0, 0, -1]], (1, 4): [[0, 0, -1], [1, 0, 0], [0, 1, 0]], (7, 5): [[0, 0, -1], [0, -1, 0], [-1, 0, 0]], (0, 5): [[0, 0, 1], [0, 1, 0], [1, 0, 0]], (4, 2): [[1, 0, 0], [0, 0, 1], [0, -1, 0]], (1, 0): [[-1, 0, 0], [0, 1, 0], [0, 0, 1]], (6, 5): [[0, 0, 1], [0, -1, 0], [-1, 0, 0]], (3, 5): [[0, 0, -1], [0, -1, 0], [1, 0, 0]], (0, 1): [[0, 1, 0], [1, 0, 0], [0, 0, 1]], (7, 0): [[-1, 0, 0], [0, -1, 0], [0, 0, -1]], (5, 2): [[-1, 0, 0], [0, 0, 1], [0, -1, 0]], (6, 1): [[0, 1, 0], [-1, 0, 0], [0, 0, -1]], (3, 1): [[0, -1, 0], [-1, 0, 0], [0, 0, 1]], (2, 4): [[0, 0, 1], [-1, 0, 0], [0, 1, 0]], (7, 4): [[0, 0, -1], [-1, 0, 0], [0, -1, 0]], (2, 0): [[1, 0, 0], [0, -1, 0], [0, 0, 1]], (4, 3): [[0, 1, 0], [0, 0, 1], [-1, 0, 0]], (2, 3): [[0, 1, 0], [0, 0, -1], [1, 0, 0]], (3, 4): [[0, 0, -1], [-1, 0, 0], [0, 1, 0]], (0, 2): [[1, 0, 0], [0, 0, 1], [0, 1, 0]]}

cayley8_from_matrices = np.zeros([48, 48], dtype=int)

all_perm_pairs1 = product(range(8), range(6))
for pair1 in all_perm_pairs1:
    mat1 = lin_transform_matrices[pair1]
    perm_props1 = position_to_permutation_properties(pair1[0], pair1[1])
    num1 = perm_props1['id_num'] if not perm_props1['perm_is_inversion'] else perm_props1['id_num']+24
    all_perm_pairs2 = product(range(8), range(6))
    for pair2 in all_perm_pairs2:
        mat2 = lin_transform_matrices[pair2]
        perm_props2 = position_to_permutation_properties(pair2[0], pair2[1])
        num2 = perm_props2['id_num'] if not perm_props2['perm_is_inversion'] else perm_props2['id_num']+24
        prod = np.dot(mat1, mat2).tolist()
        for k_pair, v_mat in lin_transform_matrices.items():
            if v_mat == prod:
                perm_props_prod = position_to_permutation_properties(k_pair[0], k_pair[1])
                num_prod = perm_props_prod['id_num'] if not perm_props_prod['perm_is_inversion'] else perm_props_prod['id_num']+24
                cayley8_from_matrices[num1, num2] = num_prod

if (cayley8_from_matrices==cayley8).all():
    print('The Cayley table made with matrix multiplication equals the one made with permutation concatenation.')





