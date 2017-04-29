from bottle import template
import numpy as np

from bin2svg import bin2svg
from dictstore import subgroup_name_to_tuple_bidict, pairs_to_num_bidict


def create_file(subgroup_name, svg_path):
    context = {'path': svg_path}
    t = template('svg_matrix_code', context)
    filename = 'files/Subgroup of Oh; {name}; matrix.svg'.format(name=subgroup_name)
    f = open(filename, 'w')
    f.write(t)
    f.close()

for sg_name, sg_tuple in subgroup_name_to_tuple_bidict.items():
    mat = np.zeros([8, 6], dtype=bool)
    for num in sg_tuple:
        pair = pairs_to_num_bidict.inv[num]
        mat[pair[0], pair[1]] = True
    svg_path = bin2svg(mat)
    create_file(sg_name, svg_path)