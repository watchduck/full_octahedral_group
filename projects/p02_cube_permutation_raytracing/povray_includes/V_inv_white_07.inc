#include "povray_includes/_cone.inc"

#declare Unit = union{
    object{Cone translate 0.5*S*y}
}

#declare Unit = union{
    object{Unit rotate 90*y}
}

#declare Unit = union{
    object{Unit}
    object{Unit rotate 180*y}
}

object{Unit}