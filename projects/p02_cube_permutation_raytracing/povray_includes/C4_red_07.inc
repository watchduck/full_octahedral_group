#declare PointA = CubeCoordinates[1];
#declare PointB = PointA - 0.5*S*x;
#declare PointC = CubeCoordinates[0];

#declare Unit = union{

    cylinder{
        PointA, PointC, Rs
        pigment{color SubgroupColorLight}
    }

    #declare HalfEdge = union{
        sphere{PointB, R}
        sphere{PointC, Rb}
        cylinder{PointB, PointC, R}
    }
    object{HalfEdge}
    object{HalfEdge rotate 180*y}

}

#declare Unit = union{
    object{Unit}
    object{
        Unit
        rotate 180*y
    }
}

#declare Unit = union{
    object{Unit}
    object{
        Unit
        rotate 90*y
    }
}

object{
    Unit
    scale -x
}