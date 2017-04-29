from bottle import template

from utils.functions import position_to_permutation_properties


def create_file(row, col):
    context = position_to_permutation_properties(row, col)
    t = template('main', context)
    filename = 'files/cube_permutation_{row}_{col}.svg'.format(row=row, col=col)
    f = open(filename, 'w')
    f.write(t)
    f.close()

for row in range(8):
    for col in range(6):
        create_file(row, col)

