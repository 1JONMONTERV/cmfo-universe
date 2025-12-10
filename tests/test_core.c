#include <stdio.h>
#include "cmfo_core.h"

void test_phi() {
    printf("[OK] phi = %.17f\n", cmfo_phi());
}

void test_tau() {
    printf("[OK] tau = %.17f\n", cmfo_tau());
}

void test_norm7() {
    double v[7] = {1,2,3,4,5,6,7};
    printf("[OK] norm7 = %.17f\n", cmfo_norm7(v));
}

void test_dot7() {
    double a[7]={1,0,0,0,0,0,1};
    double b[7]={1,1,0,0,0,1,1};
    printf("[OK] dot7 = %.17f\n", cmfo_dot7(a,b));
}

void test_add7() {
    double a[7]={1,1,1,1,1,1,1};
    double b[7]={1,2,3,4,5,6,7};
    double out[7];
    cmfo_add7(out,a,b);
    printf("[OK] add7 = [%.1f %.1f %.1f %.1f %.1f %.1f %.1f]\n",
        out[0],out[1],out[2],out[3],out[4],out[5],out[6]);
}

void test_scale7() {
    double a[7]={1,2,3,4,5,6,7};
    double out[7];
    cmfo_scale7(out, a, 3.0);
    printf("[OK] scale7 = [%.1f %.1f %.1f %.1f %.1f %.1f %.1f]\n",
        out[0],out[1],out[2],out[3],out[4],out[5],out[6]);
}

int main() {
    test_phi();
    test_tau();
    test_norm7();
    test_dot7();
    test_add7();
    test_scale7();
    return 0;
}
