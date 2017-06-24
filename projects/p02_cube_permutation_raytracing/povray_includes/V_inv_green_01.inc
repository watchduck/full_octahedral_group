#include "povray_includes/_cone.inc"

#declare Unit = object{
    Cone rotate 90*x
}

#declare Unit = union{
    object{Unit}
    object{Unit scale -x rotate 180*x}
}

object{Unit}