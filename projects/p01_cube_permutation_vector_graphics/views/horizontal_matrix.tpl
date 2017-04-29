<%
from utils.constants import matrix_line_color, matrix_background_color, matrix_border_color, matrix_border_width
%>

<g transform="translate(37, 5)">

    <g transform="scale(6)">

        <!--background-->
        <rect width="8" height="3" stroke="{{matrix_border_color}}" stroke-width="{{matrix_border_width}}"/>
        <rect width="8" height="3" stroke="none" fill="{{matrix_background_color}}"/>

        <!--entries-->
        %for m, matrow in enumerate(mat):
            %for n, entry in enumerate(matrow):
                %if entry:
                    <rect x="{{n}}" y="{{m}}" width="1" height="1" fill="#888"/>
                %end
            %end
        %end

        <!--lines-->
        <rect x="0" y="0" width="8" height="3" stroke="{{matrix_line_color}}" stroke-width=".1" fill="none"/>
        <path stroke-dasharray=".03, .97" d="M 4, -.015  v3" stroke="{{matrix_line_color}}" stroke-width="8"/>
        <g stroke="{{matrix_line_color}}" stroke-width="3">
            <path stroke-dasharray=".03, .97" d="M -.015, 1.5  h 8"/>
            <path stroke-dasharray=".1, 3.9" d="M -.05, 1.5 h 8"/>
        </g>
    </g>

    <!--numbers (1, 2, 4)-->
    <g transform="translate(-11.4, -12.6) scale(.4)" opacity=".1">
        %for m, matrow in enumerate(mat):
            %for n, entry in enumerate(matrow):
                %if entry:
                    <use x="{{n*6*2.5}}" y="{{m*6*2.5}}" xlink:href="#n{{2**m}}"/>
                %end
            %end
        %end
    </g>

</g>