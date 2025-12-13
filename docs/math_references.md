# Referencias Matemáticas y Constantes

Este documento lista las constantes fundamentales y las estructuras matemáticas utilizadas en el código fuente de `cmfo-universe` para facilitar la verificación y el mantenimiento.

## Constantes Universales

| Símbolo | Valor Aproximado | Definición Exacta | Uso en Código |
| :--- | :--- | :--- | :--- |
| $\phi$ (Phi) | 1.6180339887... | $(1 + \sqrt{5}) / 2$ | `PHI_VAL` |
| $\psi$ (Psi) | 0.6180339887... | $1 / \phi = \phi - 1$ | `PSI_VAL` |
| $\tau$ (Tau) | 6.2831853071... | $2\pi$ | `TAU_VAL` |

## Matrices Estructurales

### Matriz de Identidad T7 ($I_7$)
Utilizada para inicialización de tensores neutros.
```c
// src/cmfo_core.c
const double I7[7][7] = {
    {1,0,0,0,0,0,0},
    ...
};
```

### Tensor Métrico ($g_{ij}$)
Define la curvatura del espacio de operación. En la versión actual v1.0, asumimos un espacio plano localmente, por lo que $g_{ij} = \delta_{ij}$ (Delta de Kronecker), pero versiones futuras (v2.0) implementarán métricas hiperbólicas.

## Mapeo de Ecuaciones a Código

### Colisión
La función `cmfo_dynamics_gpu` implementa la Ec. 3.1 de `theory_solitons.md`.

*   **Entrada Code**: `double* a`, `double* b`
*   **Teoría**: $S_1, S_2$
*   **Transformación**:
    `out = a * b * phi` (simplificado) corresponde a una proyección lineal del producto fractal.

## Bibliografía Cruzada
*   [theory_solitons.md](./theory_solitons.md) - Para derivaciones completas.
