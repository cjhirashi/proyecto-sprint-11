"""
Propósito: Funciones para seleccionar pozos top-k por predicción, calcular
beneficios y elaborar resúmenes por región. Valores por defecto alineados
con el proyecto (200 pozos, inversión 100M USD, ingreso por unidad 4500).
"""

from __future__ import annotations
from typing import Dict, Tuple
import pandas as pd


def select_top_k_by_pred(
    preds_df: pd.DataFrame,
    k: int = 200,
    pred_col: str = "pred"
) -> pd.DataFrame:
    """
    Propósito: Seleccionar los k pozos con mayor predicción.

    Retorna
    -------
    pd.DataFrame con las k filas de mayor 'pred'.
    """
    # 1) Ordenar por predicción descendente
    return preds_df.sort_values(pred_col, ascending=False).head(k).copy()


def compute_profit_from_selected(
    selected_df: pd.DataFrame,
    ingreso_por_unidad: float = 4500.0,
    costos_inversion: float = 100_000_000.0,
    real_col: str = "real"
) -> float:
    """
    Propósito: Calcular beneficio total a partir de los pozos seleccionados (valores reales).

    Fórmula
    -------
    beneficio = sum(real_top_k) * ingreso_por_unidad - costos_inversion
    """
    # 1) Suma de producción real en los top-k
    total_real = float(selected_df[real_col].sum())

    # 2) Beneficio
    beneficio = total_real * ingreso_por_unidad - costos_inversion
    return float(beneficio)


def region_profit_summary(
    preds_df: pd.DataFrame,
    top_k: int = 200,
    ingreso_por_unidad: float = 4500.0,
    costos_inversion: float = 100_000_000.0,
    pred_col: str = "pred",
    real_col: str = "real",
    region_name: str | None = None
) -> Dict[str, float | str]:
    """
    Propósito: Resumen compacto del beneficio esperado por región usando top-k.

    Retorna
    -------
    dict con:
        - region
        - top_k
        - total_real_top_k
        - beneficio
    """
    # 1) Selección de pozos top-k
    top_df = select_top_k_by_pred(preds_df, k=top_k, pred_col=pred_col)

    # 2) Suma real
    total_real_top_k = float(top_df[real_col].sum())

    # 3) Beneficio
    beneficio = compute_profit_from_selected(
        top_df,
        ingreso_por_unidad=ingreso_por_unidad,
        costos_inversion=costos_inversion,
        real_col=real_col
    )

    return {
        "region": region_name or "",
        "top_k": float(top_k),
        "total_real_top_k": total_real_top_k,
        "beneficio": float(beneficio),
    }
