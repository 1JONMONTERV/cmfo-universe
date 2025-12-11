#include <stdio.h>
#include <math.h>
#include "cmfo_core.h"

static int eq(double a, double b, double eps){ return fabs(a-b) <= eps; }

int main(void){
    double I[7][7], Z[7][7], AT[7][7], ATT[7][7];
    double v[7]={1,2,3,4,5,6,7}, w[7];
    const double eps=1e-12;

    cmfo_mat7_identity(I);
    cmfo_mat7_zero(Z);

    for(int i=0;i<7;i++)
      for(int j=0;j<7;j++){
          if(I[i][j] != (i==j?1.0:0.0)){ printf("FAIL ID\n"); return 1; }
          if(Z[i][j] != 0.0){ printf("FAIL ZERO\n"); return 1; }
      }

    cmfo_mat7_transpose(AT, I);
    cmfo_mat7_transpose(ATT, AT);

    for(int i=0;i<7;i++)
      for(int j=0;j<7;j++)
        if(!eq(ATT[i][j], I[i][j], eps)){ printf("FAIL (I^T)^T\n"); return 1; }

    cmfo_mat7_vec(w, I, v);
    for(int i=0;i<7;i++)
      if(w[i] != v[i]){ printf("FAIL I*v\n"); return 1; }

    printf("[OK] test_mat7 passed\n");
    return 0;
}
