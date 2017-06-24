#declare PointA = CubeCoordinates[4];
#declare PointB = CubeCoordinates[6];
#declare PointC = CubeCoordinates[2];
#declare PointD = CubeCoordinates[3];

sphere{PointA, R}
sphere{PointB, R}
sphere{PointC, R}
sphere{PointD, R}

cylinder{PointA, PointB, R}
cylinder{PointC, PointD, R}

cylinder{
    PointB, PointC, Rs
    pigment{color SubgroupColorLight}
}
