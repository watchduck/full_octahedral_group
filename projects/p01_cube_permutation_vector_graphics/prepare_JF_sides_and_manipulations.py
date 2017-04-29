from itertools import product

from utils.functions import position_to_permutation_properties
from utils.helpers import concat


JF_cube_sides = {
    (0, 0): 'J front',
    (3, 0): 'J back',
    (2, 1): 'F front',
    (1, 1): 'F back',
    (2, 2): 'top',
    (4, 2): 'bottom'
}

manipulations = {
    (0, 0): 'nothing',
    (5, 0): '180',
    (4, 0): 'vert',
    (1, 0): 'horz',
    (4, 5): 'right',
    (1, 5): 'left',
    (0, 5): 'tlbr',
    (5, 5): 'bltr'
}

JF_sides_and_manipulations = {}

all_perm_pairs = product(range(8), range(6))

for find_pair in all_perm_pairs:
    find_perm = position_to_permutation_properties(find_pair[0], find_pair[1])['perm']

    for side_pair in JF_cube_sides.keys():
        side_perm = position_to_permutation_properties(side_pair[0], side_pair[1])['perm']

        for mani_pair in manipulations.keys():
            mani_perm = position_to_permutation_properties(mani_pair[0], mani_pair[1])['perm']

            if concat(mani_perm, side_perm) == find_perm:
                JF_sides_and_manipulations[find_pair] = (
                    JF_cube_sides[side_pair],
                    manipulations[mani_pair]
                )

print(JF_sides_and_manipulations)

# result copied to utils.constants