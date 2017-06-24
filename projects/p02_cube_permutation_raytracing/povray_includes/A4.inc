#declare D = 0.17*S;


#declare PointA = CubeCoordinates[4] + D*x - D*y;
#declare PointB = CubeCoordinates[1] - D*x + D*y;

#declare PointA_ = CubeCoordinates[4] - 2*D*y;
#declare PointB_ = CubeCoordinates[1] + 2*D*y;

#declare Unit = union{
    sphere{PointA_, R}
    sphere{PointA, R}
    sphere{PointB, R}
    sphere{PointB_, R}
    cylinder{PointA_, PointA, R}
    cylinder{PointA, PointB, R}
    cylinder{PointB, PointB_, R}
}

#declare Unit1 = union{
    object{Unit}
    object{Unit rotate 180*y}
}

#declare Unit2 = object{
    Unit1
    rotate 90*z
    rotate 90*y
}

#declare Unit3 = object{
    Unit1
    rotate 90*z
    rotate 90*x
}

object{Unit1}
object{Unit2}
object{Unit3}