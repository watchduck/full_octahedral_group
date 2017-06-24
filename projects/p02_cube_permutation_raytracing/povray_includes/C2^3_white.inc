#declare PointA = CubeCoordinates[0] + 0.5*S*y;
#declare PointB = CubeCoordinates[1] + 0.5*S*y;
#declare PointC = CubeCoordinates[3] + 0.5*S*y;
#declare PointD = CubeCoordinates[2] + 0.5*S*y;

sphere{PointA, R}
sphere{PointB, R}
sphere{PointC, R}
sphere{PointD, R}

cylinder{PointA, PointB, R}
cylinder{PointC, PointD, R}
