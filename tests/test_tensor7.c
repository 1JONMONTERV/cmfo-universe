#include <stdio.h>
#include "cmfo_core.h"

int main() {
    double a[7] = {1,2,3,4,5,6,7};
    double b[7] = {7,6,5,4,3,2,1};
    double out[7];

    cmfo_tensor7(out, a, b);

    printf("[OK] tensor7 = [");
    for (int i = 0; i < 7; i++) printf("%g%s", out[i], (i<6?", ":""));
    printf("]\n");

    return 0;
}
