"""
Propósito: Funciones de carga y preparación de datos por región.
"""

from __future__ import annotations
from typing import List, Optional, Tuple
import pandas as pd


def load_region_csv(path: str, usecols: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Propósito: Cargar el CSV de una región y regresar un DataFrame limpio.

    Parámetros
    ----------
    path : str
        Ruta al archivo CSV (por ej. 'datasets/geo_data_0.csv').
    usecols : list[str] | None
        Columnas a cargar. Si es None, carga todas.

    Retorna
    -------
    pd.DataFrame
        Datos de la región.
    """
    # 1) Cargar archivo
    df = pd.read_csv(path, usecols=usecols)

    # 2) (Opcional) Validaciones mínimas
    expected_cols = {"id", "f0", "f1", "f2", "product"}
    if not expected_cols.issubset(df.columns):
        raise ValueError(
            f"El archivo {path} no contiene las columnas esperadas: {expected_cols}."
        )

    # 3) Sin cambios estructurales aquí para mantener integridad del dataset
    return df


def prepare_features_target(
    df: pd.DataFrame,
    target_col: str = "product",
    feature_cols: Optional[List[str]] = None
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Propósito: Separar características (X) y objetivo (y) a partir del DataFrame.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame de entrada con columnas de features y target.
    target_col : str
        Nombre de la columna objetivo. Por defecto 'product'.
    feature_cols : list[str] | None
        Columnas a usar como features. Si es None, usa todas menos 'id' y 'target_col'.

    Retorna
    -------
    (X, y) : Tuple[pd.DataFrame, pd.Series]
        X con columnas de características y y con la variable objetivo.
    """
    # 1) Selección de columnas de features
    if feature_cols is None:
        feature_cols = [c for c in df.columns if c not in ("id", target_col)]

    # 2) Construcción de matrices
    X = df[feature_cols].copy()
    y = df[target_col].copy()

    return X, y
