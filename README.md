# 📊 Proyecto Sprint 11 - Selección de Región Petrolera

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-lightblue?logo=numpy)](https://numpy.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Models-orange?logo=scikitlearn)](https://scikit-learn.org/stable/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)

---

## 🚀 Descripción

Proyecto del Sprint 11 de TripleTen. La empresa OilyGiant busca determinar la **región óptima para abrir 200 pozos de petróleo**.
Se entrena un modelo de **regresión lineal** para predecir el volumen de reservas en cada región, se seleccionan los pozos más rentables y se calculan beneficios y riesgos mediante **bootstrapping (1000 muestras)**.
La región final se elige considerando el **mayor beneficio esperado** y un **riesgo de pérdidas < 2.5%**.

---

## ✨ Instrucciones y Objetivos del proyecto

1. **Descarga y preparación de datos**  
   * Cargar los tres datasets (`geo_data_0.csv`, `geo_data_1.csv`, `geo_data_2.csv`).  
   * Revisar su estructura, dimensiones y calidad.  
   * Explicar el procedimiento de carga y preparación.  

2. **Entrenamiento y prueba del modelo por región**  
   * Dividir cada dataset en entrenamiento y validación (75:25).  
   * Entrenar un modelo de **regresión lineal** en cada región.  
   * Generar predicciones en el conjunto de validación.  
   * Guardar predicciones y valores reales.  
   * Calcular y mostrar: **RMSE** y **volumen medio de reservas predicho**.  
   * Analizar resultados obtenidos.  

3. **Automatización y repetición**  
   * Colocar todos los pasos previos en funciones reutilizables.  
   * Ejecutar el flujo completo para los tres archivos (`geo_data_0`, `geo_data_1`, `geo_data_2`).  

4. **Preparación para cálculo de ganancias**  
   * Almacenar en variables los valores relevantes para los cálculos.  
   * Considerar la inversión de **100 millones USD** para 200 pozos.  
   * Calcular punto de equilibrio: cada pozo debe generar al menos **500,000 USD** (≈111.1 unidades).  
   * Comparar este valor con la media de reservas en cada región.  
   * Presentar conclusiones sobre la viabilidad inicial del cálculo de beneficio.  

5. **Cálculo de ganancias**  
   * Implementar una función que calcule la ganancia de un conjunto de pozos seleccionados.  
   * Seleccionar los **200 pozos con mayor valor de predicción** en cada región.  
   * Calcular y almacenar el volumen objetivo de reservas y la ganancia potencial.  
   * Presentar conclusiones y proponer la región más prometedora.  

6. **Cálculo de riesgos y ganancias mediante bootstrapping**  
   * Aplicar **bootstrapping con 1000 muestras** a las predicciones top-200 de cada región.  
   * Calcular: **beneficio promedio**, **intervalo de confianza al 95%** y **riesgo de pérdida (probabilidad de ganancia negativa)**.  
   * Presentar conclusiones finales: recomendar la región con mayor beneficio esperado y riesgo < 2.5%.  
   * Comparar con la elección previa del paso 5.  

---

## 🧰 Tecnologías utilizadas

* [Python 3.10](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [NumPy](https://numpy.org/)
* [Scikit-Learn](https://scikit-learn.org/stable/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Jupyter Notebook](https://jupyter.org/)
* [Conda](https://docs.conda.io/) – gestión de entornos y dependencias

---

## ✅ PASOS DEL PROYECTO

### 📒 Pasos en el Notebook

1. **Sprint 11 - Selección de Región Petrolera en OilyGiant**  
   1.1 **Objetivo del Proyecto y Contexto**  
   1.2 **Configuración Inicial**  

2. **Carga y Exploración de Datasets**  
   2.1 **Cargar Datasets**   
   2.2 **Validación de estructura y tipos de datos**  
   2.3 **Revisión de valores nulos y duplicados**  
   2.4 **Análisis exploratorio inicial**  
   2.5 **Visualización exploratoria complementaria**  

3. **Modelado y validación de predicciones**  
   3.1 **Preparación de los datos de entrenamiento y validación**  
   3.2 **Entrenamiento de modelos de regresión lineal**  
   3.3 **Evaluación de modelos en conjunto de validación**   
   3.4 **Almacenamiento de predicciones y valores reales**

4. **Estimación de beneficios y análisis de riesgos con bootstrapping**  
   4.1 **Preparación para el cálculo de beneficios**  
   4.2 **Selección de los 200 pozos más prometedores por región**   
   4.3 **Estimación del beneficio esperado por región**   
   4.4 **Bootstrapping de beneficios y riesgo por región**  
   4.5 **Visualizaciones de la distribución de beneficios**  
   - 4.5.1 Histogramas de distribución por región  
   - 4.5.2 Comparación de beneficios promedio por región  


5. **Conclusiones finales y recomendación del proyecto**  

---

### ⚙️ Pasos previstos para `src/`

- **`data_loading.py`**
  - `load_region_csv(path, usecols=None)`  
    **Atributos:**  
    - `path` (str): Ruta del archivo CSV de la región (ej. `"datasets/geo_data_0.csv"`).  
    - `usecols` (list[str] | None): Columnas a cargar; si es `None`, carga todas.  
    **Descripción:** Carga el dataset de una región y valida que existan las columnas esperadas (`id`, `f0`, `f1`, `f2`, `product`).  

  - `prepare_features_target(df, target_col="product", feature_cols=None)`  
    **Atributos:**  
    - `df` (pd.DataFrame): Datos completos de la región.  
    - `target_col` (str): Nombre de la columna objetivo; por defecto `"product"`.  
    - `feature_cols` (list[str] | None): Lista de columnas a usar como features; si es `None`, usa todas excepto `id` y la columna objetivo.  
    **Descripción:** Separa el DataFrame en variables predictoras (X) y variable objetivo (y).  

---

- **`modeling.py`**
  - `split_data(X, y, test_size=0.25, random_state=12345)`  
    **Atributos:**  
    - `X` (pd.DataFrame): Variables predictoras.  
    - `y` (pd.Series): Variable objetivo.  
    - `test_size` (float): Proporción para validación (ej. 0.25 = 25%).  
    - `random_state` (int): Semilla para reproducibilidad.  
    **Descripción:** Divide los datos en entrenamiento y validación (75:25 por defecto).  

  - `train_linear_regression(X_train, y_train)`  
    **Atributos:**  
    - `X_train` (pd.DataFrame): Features del conjunto de entrenamiento.  
    - `y_train` (pd.Series): Valores reales del conjunto de entrenamiento.  
    **Descripción:** Entrena un modelo de regresión lineal con scikit-learn.  

  - `evaluate_model(model, X_valid, y_valid)`  
    **Atributos:**  
    - `model` (LinearRegression): Modelo previamente entrenado.  
    - `X_valid` (pd.DataFrame): Features del conjunto de validación.  
    - `y_valid` (pd.Series): Valores reales del conjunto de validación.  
    **Descripción:** Evalúa el modelo en validación y devuelve métricas: **RMSE**, media de predicciones y media real.  

  - `predict_vs_real_df(model, X_valid, y_valid, pred_col="pred", real_col="real")`  
    **Atributos:**  
    - `model` (LinearRegression): Modelo entrenado.  
    - `X_valid` (pd.DataFrame): Features de validación.  
    - `y_valid` (pd.Series): Valores reales.  
    - `pred_col` (str): Nombre de la columna de predicciones.  
    - `real_col` (str): Nombre de la columna de valores reales.  
    **Descripción:** Devuelve un DataFrame con dos columnas (`pred`, `real`) para comparar predicciones y valores reales.  

---

- **`economics.py`**
  - `select_top_k_by_pred(preds_df, k=200, pred_col="pred")`  
    **Atributos:**  
    - `preds_df` (pd.DataFrame): DataFrame con columnas de predicción y valores reales.  
    - `k` (int): Número de pozos a seleccionar; por defecto 200.  
    - `pred_col` (str): Nombre de la columna de predicciones.  
    **Descripción:** Selecciona los `k` pozos con mayor valor de predicción.  

  - `compute_profit_from_selected(selected_df, ingreso_por_unidad=4500, costos_inversion=100_000_000, real_col="real")`  
    **Atributos:**  
    - `selected_df` (pd.DataFrame): DataFrame con los pozos seleccionados.  
    - `ingreso_por_unidad` (float): Ingreso en USD por cada unidad de producción (ej. 4500 USD).  
    - `costos_inversion` (float): Inversión total en USD (ej. 100,000,000).  
    - `real_col` (str): Columna con los valores reales de producción.  
    **Descripción:** Calcula el beneficio neto total usando los valores reales de los pozos seleccionados.  

  - `region_profit_summary(preds_df, top_k=200, ingreso_por_unidad=4500, costos_inversion=100_000_000, region_name=None)`  
    **Atributos:**  
    - `preds_df` (pd.DataFrame): DataFrame con predicciones y valores reales.  
    - `top_k` (int): Número de pozos a considerar (por defecto 200).  
    - `ingreso_por_unidad` (float): Ingreso en USD por unidad de producción.  
    - `costos_inversion` (float): Inversión total en USD.  
    - `region_name` (str | None): Nombre de la región (opcional).  
    **Descripción:** Devuelve un diccionario resumen con nombre de región, total real top-k y beneficio calculado.  

---

- **`bootstrap.py`**
  - `bootstrap_benefit(preds_df, ingreso_por_unidad, costos_inversion, n_iter=1000, sample_size=500, top_k=200, pred_col="pred", real_col="real", random_state=12345)`  
    **Atributos:**  
    - `preds_df` (pd.DataFrame): DataFrame con columnas de predicciones y valores reales.  
    - `ingreso_por_unidad` (float): Ingreso por unidad de producción.  
    - `costos_inversion` (float): Inversión total en USD.  
    - `n_iter` (int): Número de iteraciones de bootstrapping (ej. 1000).  
    - `sample_size` (int): Tamaño de la muestra con reemplazo en cada iteración (ej. 500 pozos).  
    - `top_k` (int): Número de pozos seleccionados por predicción en cada muestra (ej. 200).  
    - `pred_col` (str): Nombre de la columna de predicciones.  
    - `real_col` (str): Nombre de la columna de valores reales.  
    - `random_state` (int): Semilla para reproducibilidad.  
    **Descripción:** Ejecuta bootstrapping simulando campañas de exploración, retorna un vector con los beneficios simulados y un resumen con promedio, intervalo de confianza al 95% y riesgo de pérdida.  


---

## ⚙️ Estructura del proyecto

```bash
.
├── datasets/
│   ├── geo_data_0.csv       # Datos región 0
│   ├── geo_data_1.csv       # Datos región 1
│   └── geo_data_2.csv       # Datos región 2
├── notebooks/
│   └── proyecto_sprint_11.ipynb  # Notebook único con todo el desarrollo del proyecto
├── src/
│   ├── data_loading.py      # Funciones para cargar datasets y preparar variables
│   ├── modeling.py          # Funciones para entrenar y validar el modelo de regresión lineal
│   ├── economics.py          # Funciones para cálculo de beneficios y selección de pozos top-200
│   └── bootstrap.py          # Funciones para aplicar bootstrapping y evaluar riesgos/intervalos de confianza
├── reports/
│   └── figuras/             # Gráficos y visualizaciones
├── environment.yml          # Entorno reproducible con Conda
└── README.md
```

---

## 📑 Dataset

**Archivos disponibles:**

* `/datasets/geo_data_0.csv`
* `/datasets/geo_data_1.csv`
* `/datasets/geo_data_2.csv`

**Columnas:**

* `id` → Identificador único del pozo.
* `f0`, `f1`, `f2` → Características de exploración (su significado específico no es importante, pero las características en sí son significativas).
* `product` → Volumen de reservas en miles de barriles.

---

## 📊 Conclusiones y Resultados Esperados

El análisis completo permitió identificar la región óptima para abrir los 200 pozos de petróleo, considerando tanto los beneficios esperados como el riesgo de pérdidas:

- El modelo de **regresión lineal** proporcionó predicciones adecuadas del volumen de reservas en cada región.  
- El cálculo de beneficios con los **200 pozos más prometedores** mostró que la **Región 1** era competitiva en términos de ingresos.  
- El **bootstrapping (1000 iteraciones)** confirmó que la **Región 1**:
  - Obtuvo el **beneficio promedio más alto**: 4.32M USD.  
  - Presentó un **intervalo de confianza del 95%** entre 168K y 8.15M USD.  
  - Fue la **única región con riesgo de pérdida < 2.5% (1.90%)**.  
- Las **visualizaciones** reforzaron estos hallazgos, mostrando distribuciones más estables y centradas en beneficios positivos para la Región 1.  

📌 **Conclusión final**: La **Región 1** es la mejor candidata para la inversión en los 200 pozos, ya que combina el **mayor beneficio esperado** con el **menor riesgo**, cumpliendo los criterios de negocio establecidos.

---

## ▶️ Instalación y uso

1. **Clonar repositorio**

   ```bash
   git clone https://github.com/cjhirashi/proyecto-sprint-11.git
   ```

2. **Acceder a la carpeta del proyecto**

   ```bash
   cd proyecto-sprint-11
   ```

3. **Crear entorno con Conda**

   ```bash
   conda env create -f environment.yml
   ```

4. **Activar el entorno**

   ```bash
   conda activate proyecto-sprint-11
   ```

5. **Ejecutar Notebooks**

   ```bash
   jupyter notebook notebooks/
   ```

---

## ♻️ Gestión del entorno con Conda

* **Eliminar entorno**:

  ```bash
  conda env remove -n proyecto-sprint-11
  ```

* **Recrear entorno**:

  ```bash
  conda env create -f environment.yml
  ```

* **Activar entorno**:

  ```bash
  conda activate proyecto-sprint-11
  ```

* **Desactivar entorno**:

  ```bash
  conda deactivate
  ```

---

## 👨‍💻 Autor

Carlos Jiménez Hirashi 💼 Data Scientist Jr. | Python & Machine Learning
📧 [cjhirashi@gmail.com](mailto:cjhirashi@gmail.com) · 🌐 [LinkedIn](https://www.linkedin.com/in/cjhirashi)
