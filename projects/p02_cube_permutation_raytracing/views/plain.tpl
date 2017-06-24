#version 3.6;
global_settings { assumed_gamma 1.0 }
#default{ finish{ ambient 0.1 diffuse 0.9 conserve_energy}}

#include "colors.inc"
#include "math.inc"


///////////////////////////// camera and light

%if not orthographic_projection:

    #declare Camera_Position = <12, 12, -50>;
    camera{
        location Camera_Position
        right    x*image_width/image_height
        angle    6.5
        look_at  <-0.05, -0.14, -0.07>
    }

%else:

    #declare Camera_Position = <0, 0, -50>;
    camera{
        orthographic
        location Camera_Position
        right    x*image_width/image_height
        angle    5.3
        look_at  <0, 0, 0>
    }

%end

light_source{ <-400, 500, -300> color White*0.9 shadowless}

light_source{ Camera_Position  color rgb<0.9,0.9,1>*0.1 shadowless}
sky_sphere{ pigment{ White } }


///////////////////////////// JF solid

#declare LightColor = rgb<0.6, 0.55, 0.55>;
#declare DarkColor = rgb<0.005, 0.004, 0.004>;
#declare CubeColor = rgb<0.25, 0.25, 0.25>;


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


#declare LetterJFSolid = union{
    object{LetterJTail}
    object{LetterStem}
    object{LetterFBar1}
    object{LetterFBar2}
    pigment{color LightColor}
}


///////////////////////////// JF outline

#declare R = 0.03;

#declare PointFBar1a = <0.9, 2.4, 0.6>;
#declare PointFBar1b = PointFBar1a + 0.9*z;
#declare PointFBar1c = PointFBar1a - 3.5*x;
#declare PointFBar1d = PointFBar1b - 3.5*x;

#declare PointFBar2c = PointFBar1c - 0.9*y;
#declare PointFBar2d = PointFBar2c + 0.9*z;
#declare PointFBar2a = PointFBar2c + 2.6*x;
#declare PointFBar2b = PointFBar2a + 0.9*z;

#declare PointFBar3a = PointFBar2a - 0.6*y;
#declare PointFBar3b = PointFBar3a + 0.9*z;
#declare PointFBar3c = PointFBar3a - 1.3*x;
#declare PointFBar3d = PointFBar3b - 1.3*x;

#declare PointFBar4a = PointFBar3a - 0.9*y;
#declare PointFBar4b = PointFBar4a + 0.9*z;
#declare PointFBar4c = PointFBar4a - 1.3*x;
#declare PointFBar4d = PointFBar4b - 1.3*x;

#declare PointJFaceA = PointFBar4a + 0.9*x;
#declare PointJFaceB = PointFBar4b + 0.9*x;

#declare PointJEndA = <0.9, -sqrt(1.125), -sqrt(1.125)>;
#declare PointJEndB = <0.9, -sqrt(0.18), -sqrt(0.18)>;
#declare PointJEndC = PointJEndA - 0.9*x;
#declare PointJEndD = PointJEndB - 0.9*x;


#declare SmallTorus = object{
    torus {0.6, R}
    rotate 90*z
}
#declare BigTorus = object{
    torus {1.5, R}
    rotate 90*z
}
#declare Tori1 = union{
    object{SmallTorus}
    object{BigTorus}
}
#declare Tori2 = object{
    Tori1
    translate 0.9*x
}
#declare Tori = union{
    object{Tori1}
    object{Tori2}
}

#declare CutBox = box{
    <-10,-10,-10> <10,10,10>
    translate 10*y
}
#declare Tori = difference{
    object{Tori}
    object{CutBox}
}
#declare CutBox = object{
    CutBox
    rotate -45*x
}
#declare Tori = difference{
    object{Tori}
    object{CutBox}
}


#declare LetterJFOutlines = union{

    sphere{PointFBar1a, R}
    sphere{PointFBar1b, R}
    sphere{PointFBar1c, R}
    sphere{PointFBar1d, R}

    sphere{PointFBar2a, R}
    sphere{PointFBar2b, R}
    sphere{PointFBar2c, R}
    sphere{PointFBar2d, R}

    sphere{PointFBar3a, R}
    sphere{PointFBar3b, R}
    sphere{PointFBar3c, R}
    sphere{PointFBar3d, R}

    sphere{PointFBar4a, R}
    sphere{PointFBar4b, R}
    sphere{PointFBar4c, R}
    sphere{PointFBar4d, R}

    sphere{PointJEndA, R}
    sphere{PointJEndB, R}
    sphere{PointJEndC, R}
    sphere{PointJEndD, R}

    cylinder{PointFBar1a, PointFBar1b, R}
    cylinder{PointFBar1b, PointFBar1d, R}
    cylinder{PointFBar1d, PointFBar1c, R}
    cylinder{PointFBar1c, PointFBar1a, R}

    cylinder{PointFBar2a, PointFBar2b, R}
    cylinder{PointFBar2b, PointFBar2d, R}
    cylinder{PointFBar2d, PointFBar2c, R}
    cylinder{PointFBar2c, PointFBar2a, R}

    cylinder{PointFBar3a, PointFBar3b, R}
    cylinder{PointFBar3b, PointFBar3d, R}
    cylinder{PointFBar3d, PointFBar3c, R}
    cylinder{PointFBar3c, PointFBar3a, R}

    cylinder{PointFBar4a, PointFBar4b, R}
    cylinder{PointFBar4b, PointFBar4d, R}
    cylinder{PointFBar4d, PointFBar4c, R}
    cylinder{PointFBar4c, PointFBar4a, R}

    cylinder{PointFBar1c, PointFBar2c, R}
    cylinder{PointFBar1d, PointFBar2d, R}

    cylinder{PointFBar2a, PointFBar3a, R}
    cylinder{PointFBar2b, PointFBar3b, R}

    cylinder{PointFBar3c, PointFBar4c, R}
    cylinder{PointFBar3d, PointFBar4d, R}

    cylinder{PointFBar1a, PointJFaceA, R}
    cylinder{PointFBar1b, PointJFaceB, R}

    cylinder{PointJEndA, PointJEndB, R}
    cylinder{PointJEndB, PointJEndD, R}
    cylinder{PointJEndD, PointJEndC, R}
    cylinder{PointJEndC, PointJEndA, R}

    object{Tori}

    pigment{color DarkColor}

}


///////////////////////////// cube

#declare CubeCoordinates = array[8]{
    <-2.25,  2.25,  2.25>,
    < 2.25,  2.25,  2.25>,
    <-2.25, -2.25,  2.25>,
    < 2.25, -2.25,  2.25>,
    <-2.25,  2.25, -2.25>,
    < 2.25,  2.25, -2.25>,
    <-2.25, -2.25, -2.25>,
    < 2.25, -2.25, -2.25>
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


///////////////////////////// show

#declare LetterJF = union{
    object{LetterJFSolid}
    object{LetterJFOutlines}
    translate <0.85, -0.45, -0.25>
    rotate 90*y
}

#declare CubeLetterCompound = union{
    object{LetterJF}
    object{Cube}
}

object{
    CubeLetterCompound

    {{!transformations}}

}
