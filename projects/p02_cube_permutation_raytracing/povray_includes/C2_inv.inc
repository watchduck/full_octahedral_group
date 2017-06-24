#declare PointA = CubeCoordinates[0];
#declare PointB = CubeCoordinates[4];
#declare PointC = PointB + 0.5*S*x;

#declare Unit = union{
    sphere{PointA, R}
    sphere{PointB, R}
    sphere{PointC, R}
    cylinder{PointA, PointB, R}
    cylinder{PointB, PointC, R}
}

object{Unit}
object{Unit scale -x scale -y scale -z}
