#declare Dist = 0.25*S;

#declare PointA = CubeCoordinates[4] + 0.5*S*x;
#declare PointB = CubeCoordinates[1] + 0.5*S*y;
#declare PointC = CubeCoordinates[1] + 0.5*S*z;
#declare PointD = CubeCoordinates[2] + 0.5*S*x;
#declare PointE = CubeCoordinates[2] + 0.5*S*y;
#declare PointF = CubeCoordinates[4] + 0.5*S*z;

#declare PointB1 = PointB - Dist*x + Dist*y;
#declare PointB2 = PointB - Dist*y + Dist*z;
#declare PointD1 = PointD + Dist*x - Dist*z;
#declare PointD2 = PointD + Dist*y - Dist*x;
#declare PointF1 = PointF + Dist*x - Dist*z;
#declare PointF2 = PointF + Dist*z - Dist*y;



union{

    // dark

    sphere{PointB1, R}
    sphere{PointB2, R}
    cylinder{PointB, PointB1, R}
    cylinder{PointB, PointB2, R}

    sphere{PointD1, R}
    sphere{PointD2, R}
    cylinder{PointD, PointD1, R}
    cylinder{PointD, PointD2, R}

    sphere{PointF1, R}
    sphere{PointF2, R}
    cylinder{PointF, PointF1, R}
    cylinder{PointF, PointF2, R}

    sphere{PointB, Rb}
    sphere{PointD, Rb}
    sphere{PointF, Rb}


    // light

    union{
        sphere{PointA, Rs}
        sphere{PointC, Rs}
        sphere{PointE, Rs}

        cylinder{PointA, PointB, Rs}
        cylinder{PointB, PointC, Rs}
        cylinder{PointC, PointD, Rs}
        cylinder{PointD, PointE, Rs}
        cylinder{PointE, PointF, Rs}
        cylinder{PointF, PointA, Rs}

        pigment{color SubgroupColorLight}
    }

    scale -x scale -y scale -z

}