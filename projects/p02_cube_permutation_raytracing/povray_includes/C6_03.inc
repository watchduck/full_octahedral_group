#declare Dist = 0.25*S;

#declare PointA = CubeCoordinates[4] + 0.5*S*x;
#declare PointB = CubeCoordinates[1] + 0.5*S*y;
#declare PointC = CubeCoordinates[1] + 0.5*S*z;
#declare PointD = CubeCoordinates[2] + 0.5*S*x;
#declare PointE = CubeCoordinates[2] + 0.5*S*y;
#declare PointF = CubeCoordinates[4] + 0.5*S*z;

#declare PointA_ = PointB - Dist*x + Dist*y;
#declare PointB_ = PointC - Dist*z + Dist*y;
#declare PointC_ = PointD - Dist*z + Dist*x;
#declare PointD_ = PointE - Dist*y + Dist*x;
#declare PointE_ = PointF - Dist*y + Dist*z;
#declare PointF_ = PointA - Dist*x + Dist*z;

union{

    // dark

    sphere{PointA, Rb}
    sphere{PointA_, R}
    cylinder{PointA, PointA_, R}

    sphere{PointB, Rb}
    sphere{PointB_, R}
    cylinder{PointB, PointB_, R}

    sphere{PointC, Rb}
    sphere{PointC_, R}
    cylinder{PointC, PointC_, R}

    sphere{PointD, Rb}
    sphere{PointD_, R}
    cylinder{PointD, PointD_, R}

    sphere{PointE, Rb}
    sphere{PointE_, R}
    cylinder{PointE, PointE_, R}

    sphere{PointF, Rb}
    sphere{PointF_, R}
    cylinder{PointF, PointF_, R}


    // light

    union{
        cylinder{PointA, PointB, Rs}
        cylinder{PointB, PointC, Rs}
        cylinder{PointC, PointD, Rs}
        cylinder{PointD, PointE, Rs}
        cylinder{PointE, PointF, Rs}
        cylinder{PointF, PointA, Rs}

        pigment{color SubgroupColorLight}
    }

}