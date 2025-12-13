# CMFO-UNIVERSE: Numerical Tolerances Specification

This document defines the numerical tolerances and precision standards used throughout the CMFO-UNIVERSE codebase to ensure mathematical rigor and reproducibility.

## Overview

CMFO-UNIVERSE implements **φ-logic** and **T⁷ fractal algebra**, which require high numerical precision to maintain mathematical invariants. All floating-point operations use **IEEE 754 double precision** (15-17 significant decimal digits).

## Fundamental Constants

### Golden Ratio (φ)

```c
#define CMFO_PHI 1.618033988749895
```

**Precision**: 15 decimal digits  
**Rationale**: The golden ratio is fundamental to φ-logic. This precision ensures accurate computation of φ-based frequencies and geometric relationships in T⁷ space.

**Verification**: 
```c
φ² = φ + 1  // Error < 1e-15
```

### Mathematical Constants

- **π (Pi)**: `M_PI` from `<math.h>` (typically 15-17 digits)
- **e (Euler's number)**: `M_E` from `<math.h>`

## Matrix Operations (T⁷ Algebra)

### Matrix Multiplication

```c
#define CMFO_TOL_MAT_MUL 1e-14
```

**Application**: Verification of matrix multiplication results  
**Rationale**: Double precision arithmetic accumulates ~1e-15 error per operation. For 7×7 matrices (49 multiplications + 42 additions per element), we expect cumulative error ~1e-14.

**Test**: `test_mat7_mul.c`

### Matrix Inversion

```c
#define CMFO_TOL_MAT_INV 1e-12
```

**Application**: Validation that `A * inv(A) = I`  
**Rationale**: Matrix inversion involves determinant calculation (expensive) and adjugate matrix computation. Error propagation through division and multiple operations justifies 1e-12 tolerance.

**Test**: `test_mat7_stability.c` (10,000 random matrices)

**Invariant Check**:
```c
// For identity matrix verification
|A * inv(A) - I|_∞ < 1e-12
```

### Determinant Calculation

```c
#define CMFO_TOL_DET 1e-13
```

**Application**: Determinant computation via cofactor expansion  
**Rationale**: 7×7 determinant requires 5040 terms (7! permutations). Accumulated floating-point error from thousands of operations necessitates 1e-13 tolerance.

**Properties**:
- `det(A * B) = det(A) * det(B)` (within tolerance)
- `det(I) = 1.0` (exact)

## Tensor Operations

### Tensor Product

```c
#define CMFO_TOL_TENSOR 1e-14
```

**Application**: Element-wise tensor products in T⁷ space  
**Rationale**: Tensor products are element-wise multiplications with minimal error accumulation.

**Algebraic Properties** (verified in `test_tensor7_props.c`):
1. **Commutativity (symmetric)**: `A ⊗_sym B = B ⊗_sym A`
2. **Distributivity**: `A ⊗ (B + C) = A ⊗ B + A ⊗ C`
3. **Antisymmetry**: `A ⊗_antisym B = -(B ⊗_antisym A)`

All properties verified with 10,000 random test vectors.

## Soliton Simulations (Sine-Gordon)

### Energy Conservation

```c
#define CMFO_TOL_SOLITON_ENERGY 1e-6
```

**Application**: Validation of Hamiltonian conservation during soliton collision  
**Rationale**: Soliton simulations use finite-difference methods with spatial discretization (dx ≈ 0.02). Numerical integration via Riemann sums introduces discretization error ~O(dx²) ≈ 4e-4. Combined with time-stepping error, 1e-6 is appropriate.

**Theoretical Energy**:
```
E_kink = 8γ = 8/√(1 - v²)
```

**Verification**: `verify_soliton_math.py` cross-checks C implementation against analytical formula.

### Topological Charge

```c
#define CMFO_TOL_TOPOLOGICAL 1e-5
```

**Application**: Verification of topological invariants (winding number)  
**Rationale**: Topological charge is computed via discrete integration of field gradients. Spatial discretization error dominates.

**Invariant**:
```
Q = (1/2π) ∫ dφ/dx dx = ±1  (integer)
```

Tolerance allows for discretization while ensuring integer detection.

### Gamma-Step Invariant

**Definition**: In boosted frames, the Lorentz factor γ = 1/√(1 - v²) must remain consistent across transformations.

**Tolerance**: `1e-12`

**Verification**:
```c
// For velocity v
double gamma_computed = 1.0 / sqrt(1.0 - v*v);
double gamma_from_energy = E_kink / 8.0;
assert(fabs(gamma_computed - gamma_from_energy) < 1e-12);
```

## CUDA Kernel Tolerances

### GPU vs CPU Comparison

```c
#define CMFO_TOL_GPU_CPU 1e-10
```

**Application**: Validation that GPU kernels produce results consistent with CPU  
**Rationale**: GPU arithmetic may use different instruction sequences (FMA, different rounding modes). Slight variations are expected but should remain within 1e-10.

**Test**: `test_cuda.cu` compares CPU and GPU tensor operations.

### Theta Evolution (Phase Dynamics)

```c
#define CMFO_TOL_THETA 1e-8
```

**Application**: Verification of phase evolution in `cmfo_dynamics_gpu`  
**Rationale**: Phase evolution involves trigonometric functions and time-stepping. Accumulated error over many iterations justifies 1e-8.

**Evolution Equation**:
```
dθᵢ/dt = ωᵢ = φ * (i + 1)
```

## Phi-Logic Tolerances

### Boolean Convergence

```c
#define CMFO_TOL_PHI_LOGIC 1e-6
```

**Application**: Verification that φ-logic operations converge to boolean logic as φ → 1  
**Rationale**: Demonstrates that boolean logic is a degenerate case of φ-logic.

**Test**: `demo_phi_logic.py`

**Convergence Property**:
```
lim (φ → 1) [φ-AND(a,b)] = AND(a,b)  (classical boolean)
```

## Summary Table

| Operation | Tolerance | Rationale |
|-----------|-----------|-----------|
| Matrix Multiplication | `1e-14` | Accumulation over 49 ops |
| Matrix Inversion | `1e-12` | Error propagation through division |
| Determinant | `1e-13` | 5040 terms in expansion |
| Tensor Product | `1e-14` | Element-wise, minimal accumulation |
| Soliton Energy | `1e-6` | Discretization error O(dx²) |
| Topological Charge | `1e-5` | Discrete integration |
| Gamma Invariant | `1e-12` | Lorentz factor precision |
| GPU vs CPU | `1e-10` | Hardware arithmetic differences |
| Theta Evolution | `1e-8` | Time-stepping accumulation |
| Phi-Logic | `1e-6` | Convergence to boolean limit |

## References

1. **IEEE 754-2008**: Standard for Floating-Point Arithmetic
2. **Goldberg, D.** (1991): "What Every Computer Scientist Should Know About Floating-Point Arithmetic"
3. **Rajaraman, R.** (1982): "Solitons and Instantons" - Energy conservation in field theory
4. **Press et al.** (2007): "Numerical Recipes" - Error analysis for matrix operations

## Implementation Files

- **C Header**: `include/cmfo_tolerances.h`
- **Python Module**: `python/cmfo/tolerances.py`
- **Tests**: 
  - `tests/test_mat7_stability.c`
  - `tests/test_tensor7_props.c`
  - `tests/verify_soliton_math.py`

---

**Last Updated**: 2025-12-12  
**Version**: 1.0.0
