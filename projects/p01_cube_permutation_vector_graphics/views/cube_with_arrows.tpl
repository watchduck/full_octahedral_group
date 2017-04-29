<%
from utils.constants import arrow_cube_svg_coordinates, cube_edges
from utils.functions import shorten_arrow
%>

<g transform="translate(35.5, 93) scale(18, 18)">

    <!--edges-->
    <g style="stroke: gray; stroke-width:.015px;">
        %for edge in cube_edges:
            % (x1, y1) = arrow_cube_svg_coordinates[edge[0]]
            % (x2, y2) = arrow_cube_svg_coordinates[edge[1]]
            <line x1="{{x1}}" y1="{{y1}}" x2="{{x2}}" y2="{{y2}}"/>
        %end
    </g>

    <!--arrows-->
    <g stroke-width=".08">
        % to_do = set(range(8))
        %while to_do:
            % k = list(to_do)[0]
            % v = perm[k]
            % to_do -= {k}
            %if k != v:
                % c1 = arrow_cube_svg_coordinates[k]
                % c2 = arrow_cube_svg_coordinates[v]
                <g opacity=".7">
                    %if perm[perm[k]] == k:
                        % to_do -= {v}
                        % ((x1, y1), (x2, y2)) = shorten_arrow(c1, c2, 0.35, True)
                        <line x1="{{x1}}" y1="{{y1}}" x2="{{x2}}" y2="{{y2}}" stroke="#{{partition_colors[k]}}" marker-end='url(#arrowend-{{partition_colors[k]}})' marker-start='url(#arrowstart-{{partition_colors[k]}})'/>
                    %else:
                        % ((x1, y1), (x2, y2)) = shorten_arrow(c1, c2, 0.35, False)
                        <line x1="{{x1}}" y1="{{y1}}" x2="{{x2}}" y2="{{y2}}" stroke="#{{partition_colors[k]}}" marker-end='url(#arrowend-{{partition_colors[k]}})'/>
                    %end
                </g>
            %end
        %end
    </g>

    <!--vertices-->
    <g style="fill: black;">
        %for x, y in arrow_cube_svg_coordinates:
            <circle cx="{{x}}" cy="{{y}}" r=".12"/>
        %end
    </g>

</g>

<!--numbers-->
<g transform="translate(22.9, 79.35) scale(.35)" fill="white">
    %for i, (x, y) in enumerate(arrow_cube_svg_coordinates):
        <g transform="translate({{51.43*x}}, {{51.43*y}})">
            <use xlink:href="#n{{i}}"/>
        </g>
    %end
</g>