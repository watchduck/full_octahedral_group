#declare PointA = CubeCoordinates[1];
#declare PointB = CubeCoordinates[2];

sphere{PointA, R}
sphere{PointB, R}
cylinder{PointA, PointB, R}
