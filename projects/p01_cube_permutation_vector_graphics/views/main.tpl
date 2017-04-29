<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="900" height="1550">

    %include defs

    <g transform="scale(10, 10)">

        <rect width="90" height="155" fill="white" stroke="none" />

        <!--SIGNED PERMUTATION MATRIX (3x3)-->
        %include small_matrix mat=signed_perm_mat

        <!--PERMUTED LETTERS WITH NEGATORS-->
        %include permuted_letters_with_negators lp=letter_perm, np=negator_pattern

        <!--HORIZONTAL MATRIX (3x8)-->
        %include horizontal_matrix mat=horz_mat

        <!--HORIZONTAL PERMUTATION-->
        %include horizontal_permutation perm=perm

        <!--PERMUTATION MATRIX (8x8)-->
        %include permutation_matrix perm=perm, partition_colors=partition_colors

        <!--CUBE WITH ARROWS-->
        %include cube_with_arrows perm=perm, partition_colors=partition_colors

        <!--GRAY CUBE WITH NUMBERS-->
        %include cube_gray invperm=inverse_perm, perm_is_inversion=perm_is_inversion

        <!--SIDE OF THE JF LETTER COMPOUND-->
        %include JF_perm row=row, col=col

    </g>

    <!--NUMBERS IN COLORED CIRCLES (UNSCALED)-->
    %include three_numbers_in_circles id=id, id_color=id_color, id_bold=id_bold, row=row, col=col, col_is_odd=col_is_odd, perm_is_inversion=perm_is_inversion

</svg>
