<%
from utils.constants import JF_sides_and_manipulations


manipulations = {
    'fix': '',
    'cross': 'rotate(180, 22.5, 22.5)',
    'vert': 'scale(1, -1) translate(0, -45)',
    'horz': 'scale(-1, 1) translate(-45, 0)',
    'right': 'rotate(90, 22.5, 22.5)',
    'left': 'rotate(-90, 22.5, 22.5)',
    'desc': 'scale(1, -1) translate(0, -45) rotate(90, 22.5, 22.5)',
    'asc': 'scale(1, -1) translate(0, -45) rotate(-90, 22.5, 22.5)'
}

(JF_side, manipulation_name) = JF_sides_and_manipulations[(row, col)]

manipulation = manipulations[manipulation_name]

rect_color = 'white'
rect_stroke_width = '.3'
rect_stroke_color = '#ddd'
light_color = '#aaa'
dark_color = '#222'
stroke_width = '.7'
%>

<g transform="translate(4.3, 90) scale(.55)">

    <g transform="{{manipulation}}">

        %if JF_side == 'J front':

            <rect width="45" height="45" fill="{{rect_color}}" stroke="{{rect_stroke_color}}" stroke-width="{{rect_stroke_width}}"/>
            <path d="M 26 3 L 26 27 A 6 6 0 0 1 20 33 A 6 6 0 0 1 15.761719 31.242188 L 9.4023438 37.601562 A 15.000001 15 0 0 0 20 42 A 15 15 0 0 0 35 27 L 35 3 L 26 3 z "
                  fill="{{light_color}}" stroke="black" stroke-width="{{stroke_width}}"/>

        %elif JF_side == 'J back':

            <g transform="matrix(-1,0,0,1,45,0)">
                <rect height="45" width="45" fill="{{rect_color}}" stroke="{{rect_stroke_color}}" stroke-width="{{rect_stroke_width}}"/>
                <path d="m 26,3 0,24 a 6,6 0 0 1 -6,6 6,6 0 0 1 -4.238281,-1.757812 L 9.4023419,37.601562 A 15,15 0 0 0 20,42 a 15,15 0 0 0 15,-15 l 0,-24 -9,0 z"
                      fill="{{light_color}}" stroke="black" stroke-width="{{stroke_width}}"/>
                <rect y="3" x="26" height="9" width="9"
                      fill="{{dark_color}}" stroke="black" stroke-width="{{stroke_width}}"/>
                <rect y="18" x="26" height="9" width="9"
                      fill="{{dark_color}}" stroke="black" stroke-width="{{stroke_width}}"/>
            </g>

        %elif JF_side == 'F front':

            <rect width="45" height="45" fill="{{rect_color}}" stroke="{{rect_stroke_color}}" stroke-width="{{rect_stroke_width}}"/>
            <path d="m 5,42 9,0 0,-15 13,0 0,-9 -13,0 0,-6 26,0 0,-9 -35,0 z"
                  fill="{{light_color}}" stroke="black" stroke-width="{{stroke_width}}"/>

        %elif JF_side == 'F back':

            <rect width="45" height="45" fill="{{rect_color}}" stroke="{{rect_stroke_color}}" stroke-width="{{rect_stroke_width}}"/>
            <path d="m 5,3 35,0 0,39 -9,0 0,-15 -13,0 0,-9 13,0 0,-6 -26,0 z"
                  fill="{{light_color}}" stroke="black" stroke-width="{{stroke_width}}"/>
            <rect width="9" height="6.3586893" x="31" y="31.225351"
                  fill="{{dark_color}}" stroke="black" stroke-width="{{stroke_width}}"/>

        %elif JF_side == 'top':

            <rect width="45" height="45" fill="{{rect_color}}" stroke="{{rect_stroke_color}}" stroke-width="{{rect_stroke_width}}"/>
            <rect width="9" height="35" x="26" y="5"
                  fill="{{light_color}}" stroke="black" stroke-width="{{stroke_width}}"/>
            <rect width="16.595608" height="9" x="9.4043961" y="31"
                  fill="{{light_color}}" stroke="black" stroke-width="{{stroke_width}}"/>
            <rect y="31" x="9.4043961" height="9" width="6.3609123"
                  fill="{{dark_color}}" stroke="black" stroke-width="{{stroke_width}}"/>

        %elif JF_side == 'bottom':

            <rect width="45" height="45" fill="{{rect_color}}" stroke="{{rect_stroke_color}}" stroke-width="{{rect_stroke_width}}"/>
            <rect width="9" height="26" x="26" y="14"
                  fill="{{light_color}}" stroke="black" stroke-width="{{stroke_width}}"/>
            <rect y="14" x="26" height="13" width="9"
                  fill="{{light_color}}" stroke="black" stroke-width="{{stroke_width}}"/>
            <rect width="25.590981" height="9" x="9.4090242" y="5"
                  fill="{{light_color}}" stroke="black" stroke-width="{{stroke_width}}"/>

        %end

    </g>

</g>
