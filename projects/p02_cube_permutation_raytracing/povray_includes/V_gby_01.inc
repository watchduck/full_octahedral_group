#declare PointA = CubeCoordinates[0];
#declare PointB = CubeCoordinates[4];

sphere{PointA, R}
sphere{PointB, R}

cylinder{PointA, PointB, R}