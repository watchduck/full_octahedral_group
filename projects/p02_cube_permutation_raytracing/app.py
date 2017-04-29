from bottle import template
from os import system

row_transformations = {
    0: '',
    1: 'scale -x',
    2: 'scale -z',
    3: 'rotate 180*y',
    4: 'scale -y',
    5: 'rotate 180*z',
    6: 'rotate 180*x',
    7: 'scale <-1, -1, -1>'
}

col_transformations = {
    0: '',
    1: 'scale -z rotate -90*y',
    2: 'scale -y rotate -90*x',
    3: 'rotate 90*x rotate 90*z',
    4: 'rotate -90*z rotate -90*x',
    5: 'scale -x rotate -90*z'
}


def render(row, col, ortho):
    context = {
        'orthographic_projection': ortho,
        'transformations': col_transformations[col] + ' ' + row_transformations[row]
    }
    t = template('scene', context)
    f = open('scene.pov', 'w')
    f.write(t)
    f.close()

    if not ortho:
        image_size = '4000'
        folder_name = 'perspective'
        ortho_in_filename = ''
    else:
        image_size = '1500'
        folder_name = 'orthographic'
        ortho_in_filename = '_ortho'

    image_name = 'cube_permutation_{row}_{col}_JF{ortho}.png'.format(
        folder=folder_name,
        row=row,
        col=col,
        ortho=ortho_in_filename
    )

    command = 'povray scene.pov +ua +fn Height={size} Width={size} +O{name}'.format(
        size=image_size,
        name=image_name
    )

    system(command)


ortho = False

for row in range(8):
    for col in range(6):
        render(row, col, ortho)
