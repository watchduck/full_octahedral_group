<%
from utils.constants import cube_grays_dict, gray_cube_svg_coordinates, cube_edges

factor = 5.5
%>

<g transform="translate(8.5, 125)">

    <!--edges-->
    <g stroke="black" stroke-width=".25">
        %for edge in cube_edges:
            % (x1, y1) = gray_cube_svg_coordinates[edge[0]]
            % (x2, y2) = gray_cube_svg_coordinates[edge[1]]
            <line x1="{{factor*x1}}" y1="{{factor*y1}}" x2="{{factor*x2}}" y2="{{factor*y2}}"/>
        %end
    </g>

    <!--vertices-->
    %for i in range(8):
        % (x, y) = gray_cube_svg_coordinates[i]
        % hex_color = cube_grays_dict['light'] if perm_is_inversion ^ (i in [0, 3, 5, 6]) else cube_grays_dict['dark']
        <circle cx="{{factor*x}}" cy="{{factor*y}}" r="2.3" stroke="black" stroke-width=".25" fill="{{hex_color}}" />
    %end

    <!--numbers-->
    <g transform="translate(-9, -9.75) scale(.25)">
    %for i in range(8):
        % (x, y) = gray_cube_svg_coordinates[i]
        % p = invperm[i]
        <use x="{{factor*4*x}}" y="{{factor*4*y}}" xlink:href="#n{{p}}"/>
    %end
    </g>

</g>
