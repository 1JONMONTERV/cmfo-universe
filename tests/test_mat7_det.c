#include "cmfo_core.h"
#include <stdio.h>

int main(void) {
    double I[7][7];
    cmfo_mat7_identity(I);

    printf("Matriz I generada:\n");
    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7; j++)
            printf("%f ", I[i][j]);
        printf("\n");
    }

    double det = cmfo_mat7_det(I);
    printf("det(I) = %f\n", det);

    return 0;
}
