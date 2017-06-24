#declare PointA = CubeCoordinates[0] + 0.5*S*y;
#declare PointB = CubeCoordinates[1] + 0.5*S*y;

#declare Unit = union{
    sphere{PointA, R}
    sphere{PointB, R}
    cylinder{PointA, PointB, R}
}

#declare Unit1 = union{
    object{Unit}
    object{Unit rotate 180*y}
}

#declare Unit2 = object{
    Unit1
    rotate 90*x
    rotate 90*z
}

#declare Unit3 = object{
    Unit1
    rotate 90*x
    rotate 90*y
}

object{Unit1}
object{Unit2}
object{Unit3}

