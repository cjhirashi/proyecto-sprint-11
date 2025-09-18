"""
Propósito: Funciones para partición de datos, entrenamiento de regresión lineal,
predicción y evaluación (RMSE), coherente con el flujo 75:25 del proyecto.
"""

from __future__ import annotations
from typing import Dict, Tuple
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def split_data(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.25,
    random_state: int = 12345
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Propósito: Dividir el dataset en entrenamiento y validación (75:25 por defecto).

    Retorna
    -------
    X_train, X_valid, y_train, y_valid
    """
    # 1) División
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )


def train_linear_regression(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """
    Propósito: Entrenar un modelo de regresión lineal (scikit-learn).
    """
    # 1) Instanciar modelo
    model = LinearRegression()

    # 2) Entrenar
    model.fit(X_train, y_train)
    return model


def evaluate_model(
    model: LinearRegression,
    X_valid: pd.DataFrame,
    y_valid: pd.Series
) -> Dict[str, float]:
    """
    Propósito: Evaluar el modelo en conjunto de validación y calcular RMSE.

    Retorna
    -------
    dict con:
        - rmse : float
        - y_pred_mean : float (media de predicciones)
        - y_valid_mean : float (media real)
    """
    # 1) Predicciones
    preds = model.predict(X_valid)

    # 2) RMSE
    rmse = mean_squared_error(y_valid, preds, squared=False)

    # 3) Métricas auxiliares
    return {
        "rmse": float(rmse),
        "y_pred_mean": float(np.mean(preds)),
        "y_valid_mean": float(np.mean(y_valid)),
    }


def predict_vs_real_df(
    model: LinearRegression,
    X_valid: pd.DataFrame,
    y_valid: pd.Series,
    pred_col: str = "pred",
    real_col: str = "real"
) -> pd.DataFrame:
    """
    Propósito: Construir un DataFrame con columnas de predicción y valor real
    a partir de un modelo entrenado y el conjunto de validación.

    Retorna
    -------
    pd.DataFrame con columnas: [pred, real]
    """
    # 1) Predicciones
    preds = model.predict(X_valid)

    # 2) Empaquetar en DataFrame
    out = pd.DataFrame({pred_col: preds, real_col: y_valid.values})
    return out
