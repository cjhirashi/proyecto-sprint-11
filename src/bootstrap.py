"""
Propósito: Bootstrapping de beneficios por región.
Simula campañas de 500 pozos (con reemplazo), selecciona top-200 por predicción
y calcula la distribución de beneficios (promedio, IC95% y riesgo de pérdida).
"""

from __future__ import annotations
from typing import Dict, Tuple
import numpy as np
import pandas as pd


def bootstrap_benefit(
    preds_df: pd.DataFrame,
    ingreso_por_unidad: float,
    costos_inversion: float,
    n_iter: int = 1000,
    sample_size: int = 500,
    top_k: int = 200,
    pred_col: str = "pred",
    real_col: str = "real",
    random_state: int = 12345
) -> Tuple[np.ndarray, Dict[str, float]]:
    """
    Propósito: Ejecutar bootstrapping de beneficios para una región.

    Procedimiento (por iteración)
    -----------------------------
    1) Muestrear 'sample_size' pozos con reemplazo.
    2) Ordenar por 'pred' y seleccionar 'top_k' mejores.
    3) Calcular beneficio con la suma de 'real' de los top_k.
       beneficio = sum(real_top_k) * ingreso_por_unidad - costos_inversion

    Retorna
    -------
    beneficios : np.ndarray
        Vector con el beneficio de cada iteración.
    resumen : dict
        - beneficio_promedio
        - ic_95_low
        - ic_95_high
        - riesgo_perdida (proporción de beneficios < 0)
    """
    # 1) Validaciones mínimas
    if not {"pred", "real"}.issubset({pred_col, real_col} | set(preds_df.columns)):
        raise ValueError(f"preds_df debe contener columnas '{pred_col}' y '{real_col}'.")

    rng = np.random.RandomState(random_state)

    n = len(preds_df)
    idx = np.arange(n)
    beneficios = np.empty(n_iter, dtype=float)

    # 2) Iteraciones
    for i in range(n_iter):
        # 2.1) Muestra con reemplazo
        sample_idx = rng.choice(idx, size=sample_size, replace=True)
        sample_df = preds_df.iloc[sample_idx]

        # 2.2) Selección top_k por predicción
        top_df = sample_df.sort_values(pred_col, ascending=False).head(top_k)

        # 2.3) Beneficio usando valores reales
        total_real = float(top_df[real_col].sum())
        beneficio = total_real * ingreso_por_unidad - costos_inversion
        beneficios[i] = beneficio

    # 3) Métricas resumen
    beneficio_promedio = float(beneficios.mean())
    ic_low, ic_high = np.percentile(beneficios, [2.5, 97.5])
    riesgo_perdida = float((beneficios < 0).mean())

    resumen = {
        "beneficio_promedio": beneficio_promedio,
        "ic_95_low": float(ic_low),
        "ic_95_high": float(ic_high),
        "riesgo_perdida": riesgo_perdida,
    }

    return beneficios, resumen
