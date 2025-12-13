#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <cuda_runtime.h>

// Declaración del wrapper (definido en theta_cmfo_kernel.cu)
extern "C" void launch_cmfo_dynamics(double* h_out, const double* h_in, int steps, double dt);

#define EPSILON 1e-5

int main() {
    printf("=== Test: Theta CMFO Kernel (7 Modes) ===\n");

    double h_in[7] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0}; // Start at 0
    double h_out[7];
    int steps = 100;
    double dt = 0.01;

    // Ejecutar Kernel
    launch_cmfo_dynamics(h_out, h_in, steps, dt);

    // Verificar Resultados
    // Dado el kernel dummy: theta += omega * dt * steps
    // omega = 1.618 * (tid + 1)
    
    int passed = 1;
    for (int i = 0; i < 7; ++i) {
        double omega = 1.61803398875 * (i + 1);
        double expected = omega * dt * steps;
        
        // Normalización T^7 (0 a 2PI)
        while (expected > 2 * 3.141592653589793) expected -= 2 * 3.141592653589793;

        printf("Mode %d: Output=%.5f, Expected=%.5f\n", i, h_out[i], expected);
        
        if (fabs(h_out[i] - expected) > EPSILON) {
            printf("[FAIL] Mode %d mismatch.\n", i);
            passed = 0;
        }
    }

    if (passed) {
        printf("[SUCCESS] All 7 modes simulated correctly.\n");
        return 0;
    } else {
        printf("[FAILURE] Test failed.\n");
        return 1;
    }
}
