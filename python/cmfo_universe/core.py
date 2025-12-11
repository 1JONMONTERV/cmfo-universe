import math

def phi() -> float:
    """Golden ratio φ"""
    return (1 + math.sqrt(5)) / 2

def tau() -> float:
    """Golden ratio conjugate τ = φ − 1"""
    return phi() - 1

def tensor7(*vals):
    """Return a 7-component tensor"""
    if len(vals) != 7:
        raise ValueError("tensor7 requires exactly 7 values")
    return list(vals)
