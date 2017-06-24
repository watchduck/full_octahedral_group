#declare PointA = CubeCoordinates[4] + 0.5*S*x;
#declare PointB = CubeCoordinates[1] + 0.5*S*y;
#declare PointC = CubeCoordinates[1] + 0.5*S*z;
#declare PointD = CubeCoordinates[2] + 0.5*S*x;
#declare PointE = CubeCoordinates[2] + 0.5*S*y;
#declare PointF = CubeCoordinates[4] + 0.5*S*z;

sphere{PointA, R}
sphere{PointB, R}
sphere{PointC, R}
sphere{PointD, R}
sphere{PointE, R}
sphere{PointF, R}

cylinder{PointA, PointB, R}
cylinder{PointB, PointC, R}
cylinder{PointC, PointD, R}
cylinder{PointD, PointE, R}
cylinder{PointE, PointF, R}
cylinder{PointF, PointA, R}

