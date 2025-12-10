#include <stdio.h>
#include <cuda_runtime.h>

extern "C" {
    __global__ void tensor7_gpu(double*, const double*, const double*);
    __global__ void dot7_gpu(double*, const double*, const double*);
    __global__ void norm7_gpu(double*, const double*);
}

int main() {

    double h_a[7] = {1,2,3,4,5,6,7};
    double h_b[7] = {7,6,5,4,3,2,1};
    double h_out[7];

    double *d_a, *d_b, *d_out;

    cudaMalloc(&d_a, 7*sizeof(double));
    cudaMalloc(&d_b, 7*sizeof(double));
    cudaMalloc(&d_out, 7*sizeof(double));

    cudaMemcpy(d_a, h_a, 7*sizeof(double), cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, 7*sizeof(double), cudaMemcpyHostToDevice);

    tensor7_gpu<<<1,7>>>(d_out, d_a, d_b);

    cudaMemcpy(h_out, d_out, 7*sizeof(double), cudaMemcpyDeviceToHost);

    printf("[GPU] tensor7 = [");
    for (int i=0;i<7;i++) printf("%.0f ", h_out[i]);
    printf("]\n");

    // Test dot product
    double h_dot = 0;
    double *d_dot;
    cudaMalloc(&d_dot, sizeof(double));

    dot7_gpu<<<1,7>>>(d_dot, d_a, d_b);
    cudaMemcpy(&h_dot, d_dot, sizeof(double), cudaMemcpyDeviceToHost);

    printf("[GPU] dot7 = %.0f\n", h_dot);

    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_out);
    cudaFree(d_dot);

    return 0;
}
