#declare PointA = CubeCoordinates[4] + 0.5*S*x;
#declare PointB = CubeCoordinates[1] + 0.5*S*y;
#declare PointC = CubeCoordinates[1] + 0.5*S*z;
#declare PointD = CubeCoordinates[2] + 0.5*S*x;
#declare PointE = CubeCoordinates[2] + 0.5*S*y;
#declare PointF = CubeCoordinates[4] + 0.5*S*z;

#declare Unit = union{

    // dark

    sphere{PointA, R}
    sphere{PointB, R}
    cylinder{PointA, PointB, R}

    sphere{PointC, R}
    sphere{PointD, R}
    cylinder{PointC, PointD, R}

    sphere{PointE, R}
    sphere{PointF, R}
    cylinder{PointE, PointF, R}

    // light

    union{
        sphere{CubeCoordinates[0], Rbb}

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

}

object{Unit}
