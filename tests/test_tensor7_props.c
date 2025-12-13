#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "cmfo_core.h"
#include "cmfo_tolerances.h"

// Configuración
#define NUM_TESTS 10000

void rand_vec(double v[7]) {
    for (int i = 0; i < 7; i++) v[i] = ((double)rand() / RAND_MAX) * 2.0 - 1.0;
}

double vec_diff_norm(const double a[7], const double b[7]) {
    double max_diff = 0.0;
    for (int i = 0; i < 7; i++) {
        double d = fabs(a[i] - b[i]);
        if (d > max_diff) max_diff = d;
    }
    return max_diff;
}

int main() {
    printf("=== CMFO T7 Tensor Verification ===\n");
    printf("Verificando propiedades algebraicas (%d it).\n", NUM_TESTS);
    srand(1234);

    double A[7], B[7], C[7];
    double res1[7], res2[7], tmp[7];

    int errors_comm = 0;
    int errors_dist = 0;
    int errors_anti = 0;

    for (int t = 0; t < NUM_TESTS; ++t) {
        rand_vec(A);
        rand_vec(B);
        rand_vec(C);

        // 1. Conmutatividad (Prod Simetrico): A (sym) B == B (sym) A
        cmfo_tensor7_sym(res1, A, B);
        cmfo_tensor7_sym(res2, B, A);
        if (vec_diff_norm(res1, res2) > CMFO_TOL_TENSOR) errors_comm++;

        // 2. Distributividad: A (x) (B + C) == A (x) B + A (x) C
        // Usamos el producto standard cmfo_tensor7
        double B_plus_C[7];
        cmfo_add7(B_plus_C, B, C);
        cmfo_tensor7(res1, A, B_plus_C);  // LHS

        double AB[7], AC[7];
        cmfo_tensor7(AB, A, B);
        cmfo_tensor7(AC, A, C);
        cmfo_add7(res2, AB, AC);  // RHS

        if (vec_diff_norm(res1, res2) > CMFO_TOL_TENSOR) errors_dist++;

        // 3. Antisimetria: cmfo_tensor7_antisym(A, B) == -cmfo_tensor7_antisym(B, A)
        // Para tensores producto punto a punto, antisym deberia ser 0 si es conmutativo,
        // pero checamos la propiedad general de la funcion antisym.
        cmfo_tensor7_antisym(res1, A, B);
        cmfo_tensor7_antisym(tmp, B, A);

        // Negar tmp -> res2
        for (int i = 0; i < 7; i++) res2[i] = -tmp[i];

        if (vec_diff_norm(res1, res2) > CMFO_TOL_TENSOR) errors_anti++;
    }

    printf("Errores Conmutatividad: %d\n", errors_comm);
    printf("Errores Distributividad: %d\n", errors_dist);
    printf("Errores Antisimetria:    %d\n", errors_anti);

    if (errors_comm + errors_dist + errors_anti == 0) {
        printf("[PASS] Propiedades Tensoriales Verificadas.\n");
        return 0;
    } else {
        printf("[FAIL] Se encontraron inconsistencias algebraicas.\n");
        return 1;
    }
}
