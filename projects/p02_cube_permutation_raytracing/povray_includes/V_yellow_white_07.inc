#declare PointA = CubeCoordinates[4] + 0.5*S*x;
#declare PointB = CubeCoordinates[6] + 0.5*S*x;

sphere{PointA, R}
sphere{PointB, R}

cylinder{PointA, PointB, R}
