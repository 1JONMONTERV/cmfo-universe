"""
CMFO-UNIVERSE: Matrix Operations Example

This example demonstrates 7×7 matrix operations including multiplication and inversion.
"""

import sys
import os
import numpy as np

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python'))

try:
    from cmfo import CMFOCore
    from cmfo.tolerances import CMFO_TOL_MAT_INV
except ImportError:
    print("Error: CMFO module not found. Please install with: pip install -e python/")
    sys.exit(1)


def main():
    print("=== CMFO-UNIVERSE: Matrix Operations ===\n")
    
    core = CMFOCore()
    
    # Create a test matrix (7×7)
    A = np.array([
        [2.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [1.0, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 2.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 2.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 2.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 2.0],
    ])
    
    print("Matrix A (7×7 tridiagonal):")
    print(A)
    print()
    
    # Compute matrix inverse using CMFO
    print("Computing A⁻¹ using CMFO core...")
    A_inv = core.mat7_inv(A)
    
    print("Inverse A⁻¹:")
    print(A_inv)
    print()
    
    # Verify: A * A⁻¹ = I
    print("Verifying A * A⁻¹ = I...")
    product = core.mat7_mul(A, A_inv)
    identity = np.eye(7)
    
    print("A * A⁻¹:")
    print(product)
    print()
    
    # Check error
    error = np.max(np.abs(product - identity))
    print(f"Maximum error: {error:.2e}")
    print(f"Tolerance: {CMFO_TOL_MAT_INV:.2e}")
    print()
    
    if error < CMFO_TOL_MAT_INV:
        print("✅ [SUCCESS] Matrix inversion verified!")
        print(f"   Error {error:.2e} < {CMFO_TOL_MAT_INV:.2e}")
        return 0
    else:
        print("❌ [FAIL] Matrix inversion error exceeds tolerance!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
