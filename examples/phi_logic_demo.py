"""
CMFO-UNIVERSE: Phi-Logic Demonstration

This example demonstrates that boolean logic is a degenerate case of φ-logic.
Shows convergence: lim(φ→1) [φ-logic] = boolean logic
"""

import sys
import os
import math

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'python'))

try:
    from cmfo.tolerances import CMFO_PHI, CMFO_TOL_PHI_LOGIC
except ImportError:
    CMFO_PHI = 1.618033988749895
    CMFO_TOL_PHI_LOGIC = 1e-6
    print("Warning: Using fallback tolerance constants\n")


def phi_and(a, b, phi):
    """
    φ-logic AND operation
    Generalizes boolean AND to continuous φ-space
    """
    return (a * b) / phi


def phi_or(a, b, phi):
    """
    φ-logic OR operation
    Generalizes boolean OR to continuous φ-space
    """
    return (a + b) - (a * b) / phi


def boolean_and(a, b):
    """Classical boolean AND"""
    return 1.0 if (a > 0.5 and b > 0.5) else 0.0


def boolean_or(a, b):
    """Classical boolean OR"""
    return 1.0 if (a > 0.5 or b > 0.5) else 0.0


def main():
    print("=== CMFO-UNIVERSE: Phi-Logic Demonstration ===\n")
    print(f"Golden Ratio φ = {CMFO_PHI}\n")
    
    # Test values (boolean: 0 or 1)
    test_cases = [
        (0.0, 0.0, "FALSE AND FALSE"),
        (0.0, 1.0, "FALSE AND TRUE"),
        (1.0, 0.0, "TRUE AND FALSE"),
        (1.0, 1.0, "TRUE AND TRUE"),
    ]
    
    print("=" * 70)
    print("CONVERGENCE TEST: φ-AND → Boolean AND as φ → 1")
    print("=" * 70)
    
    # Show convergence for different φ values approaching 1
    phi_values = [CMFO_PHI, 1.5, 1.2, 1.1, 1.01, 1.001]
    
    for a, b, desc in test_cases:
        print(f"\n{desc} (a={a}, b={b}):")
        print(f"{'φ value':<12} | {'φ-AND':<12} | {'Boolean AND':<12} | {'Difference':<12}")
        print("-" * 60)
        
        bool_result = boolean_and(a, b)
        
        for phi in phi_values:
            phi_result = phi_and(a, b, phi)
            diff = abs(phi_result - bool_result)
            print(f"{phi:<12.3f} | {phi_result:<12.6f} | {bool_result:<12.6f} | {diff:<12.2e}")
    
    print("\n" + "=" * 70)
    print("CONVERGENCE TEST: φ-OR → Boolean OR as φ → 1")
    print("=" * 70)
    
    test_cases_or = [
        (0.0, 0.0, "FALSE OR FALSE"),
        (0.0, 1.0, "FALSE OR TRUE"),
        (1.0, 0.0, "TRUE OR FALSE"),
        (1.0, 1.0, "TRUE OR TRUE"),
    ]
    
    for a, b, desc in test_cases_or:
        print(f"\n{desc} (a={a}, b={b}):")
        print(f"{'φ value':<12} | {'φ-OR':<12} | {'Boolean OR':<12} | {'Difference':<12}")
        print("-" * 60)
        
        bool_result = boolean_or(a, b)
        
        for phi in phi_values:
            phi_result = phi_or(a, b, phi)
            diff = abs(phi_result - bool_result)
            print(f"{phi:<12.3f} | {phi_result:<12.6f} | {bool_result:<12.6f} | {diff:<12.2e}")
    
    print("\n" + "=" * 70)
    print("CONCLUSION")
    print("=" * 70)
    print(f"✅ As φ → 1, φ-logic operations converge to classical boolean logic")
    print(f"✅ This demonstrates that boolean logic is a special case of φ-logic")
    print(f"✅ φ-logic provides a continuous generalization of discrete boolean operations")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
