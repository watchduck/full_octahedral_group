<g transform="scale(.2) translate(23, -4)">
    <!--letters-->
    <g transform="translate(98, -830)">
        <use xlink:href="#{{lp[0]}}"/>
        <use xlink:href="#{{lp[1]}}" transform="translate(0, 30)"/>
        <use xlink:href="#{{lp[2]}}" transform="translate(0, 60)"/>
    </g>
    <!--negators-->
    %for k, v in enumerate(np):
        %if v:
            <path d="m 117, {{43 + k*30}} h 10 v 4" fill="none" stroke="black" stroke-width="1.4"/>
        %end
    %end
</g>