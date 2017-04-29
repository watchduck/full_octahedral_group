<%
from utils.constants import matrix_line_color, matrix_background_color, matrix_border_color, matrix_border_width
from utils.functions import svg_path_for_arrow_in_permutation_matrix
%>

<g transform="translate(37, 37) scale(6)">

    <!--background-->
    <rect width="8" height="8" stroke="{{matrix_border_color}}" stroke-width="{{matrix_border_width}}"/>
    <rect width="8" height="8" stroke="none" fill="{{matrix_background_color}}"/>

    <!--entries-->
    %for k, v in enumerate(perm):
        <rect x="{{k}}" y="{{v}}" width="1" height="1" fill="#{{partition_colors[k]}}" fill-opacity="0.7"/>
    %end

    <!--lines-->
    <rect x="0" y="0" width="8" height="8" stroke="{{matrix_line_color}}" stroke-width=".1" fill="none"/>
    <g stroke="{{matrix_line_color}}" stroke-width="8">
        <path stroke-dasharray=".03, .97" d="M -.015, 4  h 9  M 4, -.015  v 9"/>
        <path stroke-dasharray=".1, 3.9" d="M -.05, 4  h 9  M 4, -.05  v 9"/>
    </g>

    <g transform="translate(.5, .5)">

        <!--arrows-->
        %for k, v in enumerate(perm):
            %if k != v:
                % arrow_path = svg_path_for_arrow_in_permutation_matrix(k, v)
                <path stroke="#{{partition_colors[k]}}" stroke-width=".075" fill="none" d="{{arrow_path}}" marker-end='url(#arrowend-{{partition_colors[k]}})'/>
            %end
        %end

        <!--black circles-->
        %for i in range(8):
            <circle cx="{{i}}" cy="{{i}}" r=".16"/>
        %end
        <!--white numbers-->
        %for i in range(8):
            <g transform="translate(-.9, -.975) scale(.025)" fill="white">
                <use x="{{40*i}}" y="{{40*i}}" xlink:href="#n{{i}}"/>
            </g>
        %end
        
    </g>

</g>