matrix_line_color = '#fff'
matrix_background_color = '#eee'
matrix_border_color = '#888'
matrix_border_width = 0.18

cc = {  # cycle colors
    'axis': 'ff0000',
    'maindiag': '00438a',
    'bigcyc': 'ba1000',
    'with0': 'ff5500',
    'without0': 'e23287',
    'lighttetra': 'da691e',
    'darktetra': '7b2e13'
}

id_colors_dict = {
    'white': '#ffffff',
    'yellow': '#ffff7f',
    'green': '#33d42a',
    'blue': '#3375ff',
    'orange': '#ffa200',
    'red': '#ef2500',
}

cube_grays_dict = {
    'light': '#ddd',
    'dark': '#888'
}

arrow_cube_svg_coordinates = [(0, 3), (2, 3), (.6, 2.2), (2.6, 2.2), (0, 1), (2, 1), (.6, .2), (2.6, .2)]

gray_cube_svg_coordinates = [(0, 3), (2, 3), (1, 2), (3, 2), (0, 1), (2, 1), (1, 0), (3, 0)]

cube_edges = [(0,1), (2,3), (4,5), (6,7), (0,2), (1,3), (4,6), (5,7), (0,4), (1,5), (2,6), (3,7)]

JF_sides_and_manipulations = {(7, 3): ('top', 'bltr'), (1, 3): ('bottom', 'tlbr'), (3, 0): ('J back', 'nothing'), (5, 4): ('F back', 'left'), (2, 1): ('F front', 'nothing'), (6, 2): ('top', 'vert'), (5, 1): ('F back', 'vert'), (2, 5): ('J back', 'right'), (0, 3): ('bottom', 'left'), (7, 2): ('top', '180'), (4, 0): ('J front', 'vert'), (1, 2): ('bottom', '180'), (5, 5): ('J front', 'bltr'), (4, 4): ('F back', 'tlbr'), (6, 3): ('top', 'right'), (1, 5): ('J front', 'left'), (5, 0): ('J front', '180'), (0, 4): ('F back', 'right'), (3, 3): ('top', 'left'), (5, 3): ('bottom', 'right'), (4, 1): ('F back', '180'), (1, 1): ('F back', 'nothing'), (6, 4): ('F front', 'right'), (3, 2): ('top', 'horz'), (0, 0): ('J front', 'nothing'), (7, 1): ('F front', '180'), (4, 5): ('J front', 'right'), (2, 2): ('top', 'nothing'), (6, 0): ('J back', '180'), (1, 4): ('F back', 'bltr'), (7, 5): ('J back', 'left'), (0, 5): ('J front', 'tlbr'), (4, 2): ('bottom', 'nothing'), (1, 0): ('J front', 'horz'), (6, 5): ('J back', 'tlbr'), (3, 5): ('J back', 'bltr'), (0, 1): ('F back', 'horz'), (7, 0): ('J back', 'vert'), (5, 2): ('bottom', 'horz'), (6, 1): ('F front', 'vert'), (3, 1): ('F front', 'horz'), (2, 4): ('F front', 'tlbr'), (7, 4): ('F front', 'bltr'), (2, 0): ('J back', 'horz'), (4, 3): ('bottom', 'bltr'), (2, 3): ('top', 'tlbr'), (3, 4): ('F front', 'left'), (0, 2): ('bottom', 'vert')}
