#declare PointA = CubeCoordinates[0];
#declare PointB = CubeCoordinates[3];
#declare PointC = CubeCoordinates[4];
#declare PointD = CubeCoordinates[7];

#declare PointA_ = PointA + 0.5*S*z;
#declare PointB_ = PointB - 0.5*S*z;
#declare PointC_ = PointC + 0.5*S*x;
#declare PointD_ = PointD - 0.5*S*x;

union{
    cylinder{PointA, PointC, Rs}
    cylinder{PointB, PointD, Rs}
    cylinder{PointA_, PointB_, Rs}
    cylinder{PointC_, PointD_, Rs}
    pigment{color SubgroupColorLight}
}

sphere{PointA, Rb}
sphere{PointB, Rb}
sphere{PointC, Rb}
sphere{PointD, Rb}

sphere{PointA_, R}
sphere{PointB_, R}
sphere{PointC_, R}
sphere{PointD_, R}

cylinder{PointA, PointA_, R}
cylinder{PointB, PointB_, R}
cylinder{PointC, PointC_, R}
cylinder{PointD, PointD_, R}