#version 3.6;
global_settings { assumed_gamma 1.0 }
#default{ finish{ ambient 0.1 diffuse 0.9 conserve_energy}}

#include "colors.inc"
#include "math.inc"


#declare LightColor = rgb<0.6, 0.55, 0.55>;
#declare DarkColor = rgb<0.005, 0.004, 0.004>;
#declare CubeColor = rgb<0.25, 0.25, 0.25>;

#declare SubgroupColor = rgb<0.25, 0.05, 0.05>;
#declare SubgroupColorLight = rgb<0.7, 0.4, 0.2>;

#declare R = 0.085;  // radius for subgroup figure
#declare Rs = 0.45*R;
#declare Rb = 2*R;
#declare Rbb = 2.7*R;



///////////////////////////// camera and light


#declare Camera_Position = <12, 12, -50>;
camera{
    location Camera_Position
    right    x*image_width/image_height
    angle    6.7
    look_at  <-0.09, -0.14, 0.1>
}


light_source{ <-400, 500, -300> color White*0.9 shadowless}

light_source{ Camera_Position  color rgb<0.9,0.9,1>*0.1 shadowless}
sky_sphere{ pigment{ White } }


///////////////////////////// JF solid

#declare BigCyl = cylinder{ <0, 0, 0>, <0.9, 0, 0>, 1.5 }
#declare SmallCyl = cylinder{ <-0.1, 0, 0>, <1, 0, 0>, 0.6 }
#declare Ring = difference{
    object{BigCyl}
    object{SmallCyl}
}
#declare CutBox = box{
    <-10,-10,-10> <10,10,10>
    translate 10*y
}
#declare HalfRing = difference{
    object{Ring}
    object{CutBox}
}
#declare CutBox = object{
    CutBox
    rotate -45*x
    pigment{color DarkColor}
}
#declare LetterJTail = difference{
    object{HalfRing}
    object{CutBox}
}


#declare LetterStem = box{
    <0, 0, 0.6>
    <0.9, 2.4, 1.5>
}


#declare LetterFBar1 = box{
    <0, 1.5, 0.6>
    <-3, 2.4, 1.5>
}
#declare CutBox = box{
    <-10,-10,-10> <10,10,10>
    translate <-12.6, 0, 0>
    pigment{color DarkColor}
}
#declare LetterFBar1 = difference{
    object{LetterFBar1}
    CutBox
}


#declare LetterFBar2 = object{
    LetterFBar1
    translate <0, -1.5, 0>
}
#declare CutBox = object{
    CutBox
    translate <1.3, 0, 0>
}
#declare LetterFBar2 = difference{
    object{LetterFBar2}
    CutBox
}


#declare LetterJFSolid = merge{
    object{LetterJTail}
    object{LetterStem}
    object{LetterFBar1}
    object{LetterFBar2}

    pigment{color LightColor}
}



///////////////////////////// cube edges

#declare S = 4.5;

#declare CubeCoordinates = array[8]{
    <-2.25, -2.25, -2.25>,
    < 2.25, -2.25, -2.25>,
    <-2.25, -2.25,  2.25>,
    < 2.25, -2.25,  2.25>,
    <-2.25,  2.25, -2.25>,
    < 2.25,  2.25, -2.25>,
    <-2.25,  2.25,  2.25>,
    < 2.25,  2.25,  2.25>
}
#declare CubeEdgesAbstractCoordinates = array[12][2]{
    {0,1}, {2,3}, {4,5}, {6,7}, {0,2}, {1,3}, {4,6}, {5,7}, {0,4}, {1,5}, {2,6}, {3,7}
}
#declare Cube = union{
    #for(i, 0, 7)
        sphere{CubeCoordinates[i], 0.01}
    #end
    #for(i, 0, 11)
        cylinder{
            CubeCoordinates[CubeEdgesAbstractCoordinates[i][0]],
            CubeCoordinates[CubeEdgesAbstractCoordinates[i][1]],
            0.01
        }
    #end
    pigment{color CubeColor}
}


///////////////////////////// cube solid

box{
    CubeCoordinates[0]
    CubeCoordinates[7]
    pigment{color rgbt<0.9, 0.9, 0.9, 0.87> }
}


///////////////////////////// subgroup figure

#declare SubgroupFigure = union{

    #include "povray_includes/{{subgroup_name}}.inc"

    pigment{color SubgroupColor}
}

///////////////////////////// finish and show


#declare LetterJFSolid = object{
    LetterJFSolid
    translate <0.85, -0.45, -0.25>
    rotate 90*y
    scale 0.7
}

object{Cube}

#declare PermutedCompound = union{
    %if with_JF:
        object{LetterJFSolid}
    %end
    object{SubgroupFigure}
}

object{
    PermutedCompound

    {{!transformations}}

}
