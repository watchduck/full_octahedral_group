<g transform="translate(10.65, 12.2)">

    <!--top row-->
    <g transform="translate(20.4, 5.25) scale(.25)" opacity=".4">
        %for i in range(8):
            <use x="{{i*6*4}}" xlink:href="#n{{i}}"/>
        %end
    </g>

    <!--bottom row-->
    <g transform="translate(15, 4.2) scale(.4)">
        %for k, v in enumerate(perm):
            <use x="{{k*6*2.5}}" xlink:href="#n{{v}}"/>
        %end
    </g>

</g>
