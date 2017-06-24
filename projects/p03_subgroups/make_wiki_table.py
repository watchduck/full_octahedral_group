import numpy as np

from store_dicts import subgroup_name_to_tuple_bidict, pairs_to_num_bidict, det_negative


sg_name = 'C2 blue 01'
sg_tuple = subgroup_name_to_tuple_bidict[sg_name]

mat = np.zeros([8, 6], dtype=bool)
for num in sg_tuple:
    pair = pairs_to_num_bidict.inv[num]
    mat[pair[0], pair[1]] = True

html_str = '''{| class="wikitable" style="margin-left: auto; margin-right: auto; border: none;"
!style="height: 25px;"|
! [[File:Finite permutation number 0.svg|20px]]
! [[File:Finite permutation number 1.svg|20px]]
! [[File:Finite permutation number 2.svg|20px]]
! [[File:Finite permutation number 3.svg|20px]]
! [[File:Finite permutation number 4.svg|20px]]
! [[File:Finite permutation number 5.svg|20px]]
'''

for i in range(8):
    html_str += '|-\n! [[File:Cube vertex number {i}.svg|20px]]\n'.format(i=i)
    for j in range(6):
        if det_negative[i][j]:
            bg_color = '#ddd'
            red = '#d00'
        else:
            bg_color = '#fff'
            red = '#f00'
        border_color = red if mat[i, j] else bg_color
        html_str += '|style="background:{bg}; padding: 0;"| <div style="margin: 2px; border: 2px solid {border}; padding: 3px;>[[File:Cube permutation {i} {j}; subgroup {name}.png|85px]]</div>\n'.format(
            i=i,
            j=j,
            name=sg_name,
            bg=bg_color,
            border=border_color
        )
html_str += '|}<noinclude>[[Category:Full octahedral group; matrices with solid permutations]]</noinclude>'


f = open('wiki_table.txt', 'w')
f.write(html_str)
f.close()