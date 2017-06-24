#declare PointA = CubeCoordinates[0];
#declare PointB = PointA + 0.75*S*z;

#declare Cone = union{
    sphere{PointA, 2.2*R}
    sphere{PointB, 0.7*R}
    cone{
        PointA, 2.2*R
        PointB, 0.7*R
    }
}