#include "cmfo_core.h"
#include <stdio.h>

// Test: multiplicación de matrices 77
int main(void) {
    double I[7][7];
    double Z[7][7];
    double C[7][7];

    cmfo_mat7_identity(I);
    cmfo_mat7_zero(Z);

    // C = I * I    debe dar I
    cmfo_mat7_mul(C, I, I);

    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7; j++) {
            if ((i == j && C[i][j] != 1.0) ||
                (i != j && C[i][j] != 0.0)) {

                printf("[FAIL] mat7_mul identity test\n");
                return 1;
            }
        }
    }

    printf("[OK] mat7_mul identity test PASSED\n");
    return 0;
}
