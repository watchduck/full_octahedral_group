#declare PointA = CubeCoordinates[0];
#declare PointB = CubeCoordinates[4];
#declare PointC = CubeCoordinates[3];
#declare PointD = CubeCoordinates[7];

sphere{PointA, R}
sphere{PointB, R}
sphere{PointC, R}
sphere{PointD, R}

cylinder{PointA, PointB, R}
cylinder{PointC, PointD, R}
