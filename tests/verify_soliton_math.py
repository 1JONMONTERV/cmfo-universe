import math
import sys

# Verification Script for Sine-Gordon Mathematics
# Rigor Level: High (Double Precision check independent of C code)

def theoretical_kink_energy(v):
    """
    Calculates the Theoretical Energy of a Sine-Gordon Kink.
    E_exact = 8 * gamma = 8 / sqrt(1 - v^2)
    """
    if abs(v) >= 1.0:
        raise ValueError("Velocity must be < 1.0")
    gamma = 1.0 / math.sqrt(1.0 - v**2)
    return 8.0 * gamma

def discretized_energy_check(N, dx, v, x0):
    """
    Simulates the C-code discrete Hamiltonian (Riemann Sum) in Python
    to verify if the C algorithm is mathematically sound (converges to 8*gamma).
    """
    # Replicate cmfo_init_kink logic independent of C
    gamma = 1.0 / math.sqrt(1.0 - v*v)
    
    phi = []
    phi_t = []
    x_vals = []
    
    # Generate Grid
    x_min = -10.0 # Standard test range
    
    # Assuming the C test uses roughly this range centered at 0
    # Recalculate dx based on N to match C behavior if needed, 
    # but here we just check if logic holds for a given discretization.
    # Logic in C: x = x_min + i * dx
    
    for i in range(N):
        x = x_min + i * dx
        x_vals.append(x)
        
        # Exact Solution
        arg = gamma * (x - x0)
        val = 4.0 * math.atan(math.exp(arg))
        
        # Derivative
        sech = 1.0 / math.cosh(arg)
        phi_x = 2.0 * gamma * sech
        vel = -v * phi_x
        
        phi.append(val)
        phi_t.append(vel)

    # Calculate Discrete Hamiltonian (Replicating cmfo_energy_sg)
    H = 0.0
    for i in range(N - 1):
        # Kinetic
        kin = 0.5 * phi_t[i]**2
        
        # Elastic
        dphi = (phi[i+1] - phi[i]) / dx
        elas = 0.5 * dphi**2
        
        # Potential
        pot = 1.0 - math.cos(phi[i])
        
        H += (kin + elas + pot) * dx
        
    return H

def main():
    print("=== CMFO: Verificacion Matematica Cruzada (Python vs Theory) ===")
    
    # Parametros de Prueba (Simulan test_soliton_collision.c)
    velocities = [0.0, 0.2, 0.5, 0.9]
    N = 1000
    L = 20.0 # -10 to 10
    dx = L / (N - 1)
    
    print(f"Propiedades de Grilla: N={N}, dx={dx:.4f}")
    print("-" * 60)
    print(f"{'Velocidad (v)':<15} | {'Energia Teorica':<18} | {'Energia Discreta':<18} | {'Error Relativo':<15}")
    print("-" * 60)
    
    all_passed = True
    
    for v in velocities:
        try:
            E_theo = theoretical_kink_energy(v)
            E_disc = discretized_energy_check(N, dx, v, 0.0)
            
            error = abs(E_theo - E_disc) / E_theo
            
            print(f"{v:<15.2f} | {E_theo:<18.6f} | {E_disc:<18.6f} | {error:<15.2e}")
            
            # Criterio de Aceptacion: < 1% error para discretización N=1000
            if error > 1e-2:
                all_passed = False
                print(f"  [FAIL] Error excedió 1% para v={v}")
        except Exception as e:
            print(f"Error calculando para v={v}: {e}")
            all_passed = False

    print("-" * 60)
    
    # Cross-Check Logic
    if all_passed:
        print("[SUCCESS] La formulación discreta en Python converge a la teoría.")
        print("          Esto valida la lógica matemática usada en cmfo_energy_sg (C).")
        sys.exit(0)
    else:
        print("[FAIL] Discrepancias significativas detectadas.")
        sys.exit(1)

if __name__ == "__main__":
    main()
