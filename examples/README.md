# CMFO-UNIVERSE Examples

This directory contains runnable examples demonstrating various features of CMFO-UNIVERSE.

## Available Examples

### 1. Basic Tensor Operation (`basic_tensor.py`)

Demonstrates basic tensor product operations in T⁷ space.

**Run:**
```bash
python examples/basic_tensor.py
```

**Expected Output:**
```
=== CMFO-UNIVERSE: Basic Tensor Operation ===

Vector A: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
Vector B: [7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]

Tensor Product (A ⊗ B): [7.0, 12.0, 15.0, 16.0, 15.0, 12.0, 7.0]

Expected: [7.0, 12.0, 15.0, 16.0, 15.0, 12.0, 7.0]

✅ [SUCCESS] Tensor product computed correctly!
```

### 2. Matrix Operations (`matrix_operations.py`)

Demonstrates 7×7 matrix multiplication and inversion with numerical verification.

**Run:**
```bash
python examples/matrix_operations.py
```

**Expected Output:**
```
=== CMFO-UNIVERSE: Matrix Operations ===

Matrix A (7×7 tridiagonal):
[[2. 1. 0. 0. 0. 0. 0.]
 [1. 2. 1. 0. 0. 0. 0.]
 ...
 [0. 0. 0. 0. 0. 1. 2.]]

Computing A⁻¹ using CMFO core...
Inverse A⁻¹:
[[ 0.667 -0.333  0.167 ...]
 [-0.333  0.833 -0.500 ...]
 ...]

Verifying A * A⁻¹ = I...
Maximum error: 2.22e-15
Tolerance: 1.00e-12

✅ [SUCCESS] Matrix inversion verified!
   Error 2.22e-15 < 1.00e-12
```

### 3. Phi-Logic Demonstration (`phi_logic_demo.py`)

Shows that boolean logic is a degenerate case of φ-logic, demonstrating convergence as φ → 1.

**Run:**
```bash
python examples/phi_logic_demo.py
```

**Expected Output:**
```
=== CMFO-UNIVERSE: Phi-Logic Demonstration ===

Golden Ratio φ = 1.618033988749895

======================================================================
CONVERGENCE TEST: φ-AND → Boolean AND as φ → 1
======================================================================

TRUE AND TRUE (a=1.0, b=1.0):
φ value      | φ-AND        | Boolean AND  | Difference  
------------------------------------------------------------
1.618        | 0.618034     | 1.000000     | 3.82e-01
1.500        | 0.666667     | 1.000000     | 3.33e-01
1.200        | 0.833333     | 1.000000     | 1.67e-01
1.100        | 0.909091     | 1.000000     | 9.09e-02
1.010        | 0.990099     | 1.000000     | 9.90e-03
1.001        | 0.999001     | 1.000000     | 9.99e-04

...

✅ As φ → 1, φ-logic operations converge to classical boolean logic
✅ This demonstrates that boolean logic is a special case of φ-logic
✅ φ-logic provides a continuous generalization of discrete boolean operations
```

## Requirements

All examples require:
- Python 3.8+
- CMFO-UNIVERSE Python package installed (`pip install -e python/`)
- NumPy (for matrix examples)

## Notes

- Examples use tolerance constants from `cmfo.tolerances` module
- All examples include verification and expected output
- Exit codes: 0 = success, 1 = failure
