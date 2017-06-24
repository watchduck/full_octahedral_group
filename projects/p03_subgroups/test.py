from sympy.combinatorics import Permutation
from sympy.combinatorics.perm_groups import PermutationGroup

from store_dicts import pairs_to_num_bidict, pairs_to_perm_bidict, subgroup_name_to_tuple_bidict


pa = Permutation([0, 2, 4, 6, 1, 3, 5, 7])
pb = Permutation([4, 0, 6, 2, 5, 1, 7, 3])
pc = Permutation([7, 6, 5, 4, 3, 2, 1, 0])
octahedral = PermutationGroup(pa, pb, pc)

all_are_subgroups = True

for sg_name, sg_tuple in subgroup_name_to_tuple_bidict.items():
    perms = []
    for el_num in sg_tuple:
        el_pair = pairs_to_num_bidict.inv[el_num]
        el_perm = pairs_to_perm_bidict[el_pair]
        el_perm = Permutation(el_perm)
        perms.append(el_perm)
    sg_group = PermutationGroup(el_perm)
    if not sg_group.is_subgroup(octahedral):
        all_are_subgroups = False

if all_are_subgroups:
    print('All tuples in ``subgroup_name_to_tuple_bidict`` represent subgroups of the full octahedral group.')