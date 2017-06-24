% from utils.constants import matrix_line_color, matrix_background_color, matrix_border_color, matrix_border_width

<g transform="translate(5, 5) scale(6)">

    <!--background-->
    <rect width="3" height="3" stroke="{{matrix_border_color}}" stroke-width="{{matrix_border_width}}"/>
    <rect width="3" height="3" stroke="none" fill="{{matrix_background_color}}"/>

    <!--entry rectangles-->
    %for m, matrow in enumerate(mat):
        %for n, matentry in enumerate(matrow):
            %if matentry != 0:
                %if matentry == 1:
                    % color = '#090'
                %else:
                    % color = '#e00'
                %end
                <rect x="{{n}}" y="{{m}}" width="1" height="1" fill="{{color}}"/>
            %end
        %end
    %end

    <!--entry signs (+, -, 0)-->
    %for m, matrow in enumerate(mat):
        %for n, matentry in enumerate(matrow):
            <g transform="translate({{n}}, {{m}}) scale(.2) translate(1, 1)">
                %if matentry != 0:
                    <rect y="1" width="3" height="1" fill="white"/>
                    %if matentry == 1:
                        <rect x="1" width="1" height="3" fill="white"/>
                    %end
                %else:
                    <circle cx="1.5" cy="1.5" r="1.2" stroke="black" stroke-width="1" fill="none" opacity=".05" />
                %end
            </g>
        %end
    %end

    <!--lines-->
    <rect x="0" y="0" width="3" height="3" stroke="{{matrix_line_color}}" stroke-width=".1" fill="none"/>
    <path stroke-dasharray=".03, .97" d="M -.015, 1.5  h4 M 1.5, -.015 v 4" stroke="{{matrix_line_color}}" stroke-width="3"/>

</g>
