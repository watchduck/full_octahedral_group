#declare PointA = CubeCoordinates[1];
#declare PointB = CubeCoordinates[2];

#declare Unit = union{
    sphere{PointA, R}
    sphere{PointB, R}
    cylinder{PointA, PointB, R}
}

#declare Unit = union{
    object{Unit}
    object{Unit rotate 180*z}
}

object{Unit}