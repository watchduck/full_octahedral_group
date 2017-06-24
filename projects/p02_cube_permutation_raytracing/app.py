from bottle import template
from os import system
from re import escape

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


def render_plain(row, col, ortho):
    context = {
        'orthographic_projection': ortho,
        'transformations': col_transformations[col] + ' ' + row_transformations[row]
    }
    t = template('plain', context)
    f = open('delete_me_after_use.pov', 'w')
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

    command = 'povray delete_me_after_use.pov +ua +fn Height={size} Width={size} +O{name}'.format(
        size=image_size,
        name=image_name
    )

    system(command)


def render_subgroup(row, col, subgroup_name, with_JF):
    context = {
        'transformations': col_transformations[col] + ' ' + row_transformations[row],
        'subgroup_name': subgroup_name,
        'with_JF': with_JF
    }
    t = template('subgroup', context)
    f = open('delete_me_after_use.pov', 'w')
    f.write(t)
    f.close()

    if with_JF:
        image_size = 2000
        image_name = 'cube_permutation_{row}_{col},_subgroup_{subgroup_name}.png'.format(
            row=row,
            col=col,
            subgroup_name=subgroup_name
        )
    else:
        image_size = 4000
        image_name = 'Subgroup_of_Oh,_{subgroup_name},_example_solid.png'.format(
            subgroup_name=escape(subgroup_name)
        )

    command = 'povray delete_me_after_use.pov +ua +fn Height={size} Width={size} +O{name} -D'.format(
        name=image_name,
        size=image_size
    )
    system(command)

    old_image_name = image_name
    image_name = image_name.replace(',', '\;')

    command = 'mv {name_with_comma} {name_with_semicolon}'.format(
        name_with_comma=old_image_name,
        name_with_semicolon=image_name
    )
    system(command)

    folder_name = subgroup_name if with_JF else 'SOLID_ONLY'
    command = 'mv {image_name} FILES/{folder_name}'.format(
        image_name=image_name,  # paretheses already escaped, semicolon already added with backslash
        folder_name=folder_name
    )
    system(command)


subgroup_names = [
    # 24
    'S4_green_orange',
    'S4_blue_red',

    'A4xC2',

    # 16
    'Dih4xC2_07',

    # 12
    'A4',

    'Dih6_03',

    # 8
    'C2^3_white',
    'C2^3_green_07',

    'C4xC2_07',

    'Dih4_green_orange_07',
    'Dih4_blue_red_07',
    'Dih4_green_red_07',
    'Dih4_blue_orange_07',

    # 6
    'S3_green_03',
    'S3_blue_03',

    'C6_03',

    # 4
    'C4_orange_07',
    'C4_red_07',

    'V_white',
    'V_green_white_07',
    'V_blue_white_07',
    'V_gby_01',
    'V_yellow_white_07',
    'V_inv_white_07',
    'V_inv_green_01',

    # 3
    'C3_03',

    # 2
    'C2_white_07',
    'C2_green_01',
    'C2_inv',
    'C2_yellow_07',
    'C2_blue_01'
]

cuboctahedral_subgroup_figures = [
    'A4_(cuboctahedron)',
    'A4xC2_(cuboctahedron)',
    'S4_green_orange_(cuboctahedron)'
]


system('mkdir FILES')

for subgroup_name in subgroup_names:
    command = 'mkdir FILES/{name}'.format(
        name=subgroup_name
    )
    system(command)
    for row in range(8):
        for col in range(6):
            render_subgroup(row, col, subgroup_name, True)


system('mkdir FILES/SOLID_ONLY')
for subgroup_name in subgroup_names + cuboctahedral_subgroup_figures:
    render_subgroup(0, 0, subgroup_name, False)
