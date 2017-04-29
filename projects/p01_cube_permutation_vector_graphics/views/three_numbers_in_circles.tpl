<%
from utils.constants import id_colors_dict, cube_grays_dict


col_stroke_width = .25 if col != 0 else .5
col_font_weight = 'normal' if col != 0 else 'bold'
col_hex_color = id_colors_dict['white'] if col in [0, 3, 4] else id_colors_dict['green']

row_hex_color = cube_grays_dict['dark'] if perm_is_inversion else cube_grays_dict['light']

perm_stroke_width = 0.285 if not id_bold else 0.57
perm_font_weight = 'normal' if not id_bold else 'bold'
perm_hex_color = id_colors_dict[id_color]
%>

<g transform="scale(10, 10) translate(20, 61)">

    <!--gray rectancles around circle with permutation ID-->
    %if col_is_odd or perm_is_inversion:
        <g fill="black" opacity=".2">
            %if col_is_odd:
                <rect x="-2.5" y="-7.5" width="5" height="15"/>
            %end
            %if perm_is_inversion:
                <rect x="-7.5" y="-2.5" width="15" height="5"/>
            %end
        </g>
    %end

    <!--circle for row number-->
    <circle cx="-11" cy="0" r="2.3" stroke="black" stroke-width=".25" fill="{{row_hex_color}}" />
    <!--circle for col number-->
    <circle cx="0" cy="-11" r="2.3" stroke="black" stroke-width="{{col_stroke_width}}" fill="{{col_hex_color}}" />
    <!--circle for permutation ID-->
    <circle cx="0" cy="0" r="3.42" stroke="black" stroke-width="{{perm_stroke_width}}" fill="{{perm_hex_color}}" />

</g>

<!--row number-->
<g style="text-anchor: middle; font-family: sans-serif; font-size: 29px; font-weight: normal;">
    <text x="90" y="620.5">{{row}}</text>
</g>
<!--col number-->
<g style="text-anchor: middle; font-family: sans-serif; font-size: 29px; font-weight: {{col_font_weight}}">
    <text x="200.1" y="510.5">{{col}}</text>
</g>
<!--permutation ID-->
<g style="text-anchor: middle; font-family: sans-serif; font-size: 33px; font-weight: {{perm_font_weight}}">
    <text x="199.5" y="622.5">{{id}}</text>
</g>
