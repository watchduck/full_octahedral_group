#declare PointA = CubeCoordinates[4];
#declare PointA_ = PointA + 0.5*S*x;

#declare PointB = CubeCoordinates[7];
#declare PointB_ = PointB - 0.5*S*x;

#declare Unit = union{

    union{
        cylinder{PointA, PointB, Rs}
        cylinder{PointA_, PointB_, Rs}
        pigment{color SubgroupColorLight}
    }

    #declare HalfEdge = union{
        sphere{PointA, Rb}
        sphere{PointA_, R}
        cylinder{PointA, PointA_, R}
    }
    object{HalfEdge}
    object{HalfEdge rotate 180*y}

}

object{Unit}
object{
    Unit
    scale -y
    rotate 90*y
}