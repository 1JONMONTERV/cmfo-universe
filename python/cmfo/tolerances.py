"""
CMFO-UNIVERSE: Numerical Tolerances (Python Module)

This module defines numerical tolerance constants mirroring the C header
cmfo_tolerances.h to ensure consistent precision across language bindings.

See Docs/NUMERICAL_TOLERANCES.md for detailed rationale.
"""

# ============================================================================
# FUNDAMENTAL CONSTANTS
# ============================================================================

#: Golden Ratio (φ) - Fundamental to φ-logic
#: Precision: 15 decimal digits
CMFO_PHI = 1.618033988749895

# ============================================================================
# MATRIX OPERATIONS (T⁷ Algebra)
# ============================================================================

#: Tolerance for matrix multiplication verification
CMFO_TOL_MAT_MUL = 1e-14

#: Tolerance for matrix inversion verification (A * inv(A) = I)
CMFO_TOL_MAT_INV = 1e-12

#: Tolerance for determinant calculation
CMFO_TOL_DET = 1e-13

# ============================================================================
# TENSOR OPERATIONS
# ============================================================================

#: Tolerance for tensor product operations
CMFO_TOL_TENSOR = 1e-14

# ============================================================================
# SOLITON SIMULATIONS (Sine-Gordon)
# ============================================================================

#: Tolerance for energy conservation in soliton dynamics
CMFO_TOL_SOLITON_ENERGY = 1e-6

#: Tolerance for topological charge (winding number)
CMFO_TOL_TOPOLOGICAL = 1e-5

#: Tolerance for Lorentz gamma factor invariant
CMFO_TOL_GAMMA = 1e-12

# ============================================================================
# CUDA KERNEL TOLERANCES
# ============================================================================

#: Tolerance for GPU vs CPU result comparison
CMFO_TOL_GPU_CPU = 1e-10

#: Tolerance for theta (phase) evolution in dynamics kernels
CMFO_TOL_THETA = 1e-8

# ============================================================================
# PHI-LOGIC
# ============================================================================

#: Tolerance for φ-logic convergence to boolean logic
CMFO_TOL_PHI_LOGIC = 1e-6

# ============================================================================
# GENERAL UTILITIES
# ============================================================================

#: Default tolerance for general floating-point comparisons
CMFO_TOL_DEFAULT = 1e-12

#: Machine epsilon for double precision
CMFO_EPSILON = 2.220446049250313e-16


__all__ = [
    'CMFO_PHI',
    'CMFO_TOL_MAT_MUL',
    'CMFO_TOL_MAT_INV',
    'CMFO_TOL_DET',
    'CMFO_TOL_TENSOR',
    'CMFO_TOL_SOLITON_ENERGY',
    'CMFO_TOL_TOPOLOGICAL',
    'CMFO_TOL_GAMMA',
    'CMFO_TOL_GPU_CPU',
    'CMFO_TOL_THETA',
    'CMFO_TOL_PHI_LOGIC',
    'CMFO_TOL_DEFAULT',
    'CMFO_EPSILON',
]
