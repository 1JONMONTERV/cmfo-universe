/*
 * Test de matriz inversa CMFO 7×7
 */

#include "cmfo_core.h"
#include <stdio.h>

void print7(double M[7][7]) {
    for (int i=0;i<7;i++) {
        for (int j=0;j<7;j++)
            printf("%f ", M[i][j]);
        printf("\n");
    }
}

int main(void) 
{
    double I[7][7];
    cmfo_mat7_identity(I);

    double Inv[7][7];
    int ok = cmfo_mat7_inv(Inv, I);

    if (!ok) {
        printf("[FAIL] inverse() failed\n");
        return 1;
    }

    double R[7][7];
    cmfo_mat7_mul_std(R, I, Inv);   // VALIDACIÓN REAL

    // Comprobar identidad
    for (int i=0;i<7;i++) {
        for (int j=0;j<7;j++) {
            double expected = (i==j)?1.0:0.0;
            if (R[i][j] != expected) {
                printf("[FAIL] I*Inv != I\n");
                print7(R);
                return 1;
            }
        }
    }

    printf("[OK] inverse(I) passed\n");
    return 0;
}
