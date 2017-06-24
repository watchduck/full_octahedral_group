#declare PointA = CubeCoordinates[0] + 0.5*S*z;
#declare PointB = CubeCoordinates[1] + 0.5*S*z;

#declare Unit = union{
    sphere{PointA, R}
    sphere{PointB, R}
    cylinder{PointA, PointB, R}
}

#declare Unit = union{
    object{Unit}
    object{
        Unit
        rotate 90*y
        rotate 180*z
    }
}

object{Unit}