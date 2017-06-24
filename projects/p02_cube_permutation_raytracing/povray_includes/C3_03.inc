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

#declare Unit = union{

    // dark

    sphere{PointA_, R}
    sphere{PointA, Rb}
    cylinder{PointA, PointA_, R}

    sphere{PointC_, R}
    sphere{PointC, Rb}
    cylinder{PointC, PointC_, R}

    sphere{PointE_, R}
    sphere{PointE, Rb}
    cylinder{PointE, PointE_, R}


    // light

    union{
        sphere{CubeCoordinates[0], Rbb}

        sphere{PointB, Rs}
        sphere{PointD, Rs}
        sphere{PointF, Rs}

        cylinder{PointA, PointB, Rs}
        cylinder{PointB, PointC, Rs}
        cylinder{PointC, PointD, Rs}
        cylinder{PointD, PointE, Rs}
        cylinder{PointE, PointF, Rs}
        cylinder{PointF, PointA, Rs}

        pigment{color SubgroupColorLight}
    }

}

object{Unit}
