"""
CMFO-UNIVERSE: Basic Tensor Operation Example

This example demonstrates basic tensor product operations in T⁷ space.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python'))

try:
    from cmfo import CMFOCore
except ImportError:
    print("Error: CMFO module not found. Please install with: pip install -e python/")
    sys.exit(1)


def main():
    print("=== CMFO-UNIVERSE: Basic Tensor Operation ===\n")
    
    # Initialize CMFO core
    core = CMFOCore()
    
    # Define two T⁷ vectors
    a = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    b = [7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
    
    print("Vector A:", a)
    print("Vector B:", b)
    print()
    
    # Compute tensor product
    result = core.tensor7(a, b)
    
    print("Tensor Product (A ⊗ B):", result)
    print()
    
    # Expected output (element-wise multiplication):
    # [7.0, 12.0, 15.0, 16.0, 15.0, 12.0, 7.0]
    expected = [a[i] * b[i] for i in range(7)]
    print("Expected:", expected)
    print()
    
    # Verify
    match = all(abs(result[i] - expected[i]) < 1e-12 for i in range(7))
    if match:
        print("✅ [SUCCESS] Tensor product computed correctly!")
    else:
        print("❌ [FAIL] Tensor product mismatch!")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
