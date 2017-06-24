#declare PointA = CubeCoordinates[0];
#declare PointB = CubeCoordinates[1];
#declare PointC = CubeCoordinates[3];
#declare PointD = CubeCoordinates[2];

sphere{PointA, R}
sphere{PointB, R}
sphere{PointC, R}
sphere{PointD, R}

cylinder{PointA, PointB, R}
cylinder{PointB, PointC, R}
cylinder{PointC, PointD, R}
cylinder{PointD, PointA, R}