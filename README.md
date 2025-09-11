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

1. **Encabezado y configuración inicial**  
   - Objetivo del proyecto y explicación del contexto.  
   - Importación de librerías y configuración visual.  

2. **Carga y exploración de datasets**  
   - Cargar los tres archivos `geo_data_0.csv`, `geo_data_1.csv`, `geo_data_2.csv`.  
   - Revisión de dimensiones, tipos de datos y primeras filas.  
   - Validación de nulos y valores atípicos.  

3. **Entrenamiento y validación de modelos por región**  
   - División 75:25 en entrenamiento y validación.  
   - Entrenamiento de regresión lineal.  
   - Generación de predicciones en el conjunto de validación.  
   - Cálculo de **RMSE** y volumen medio de reservas predicho.  
   - Análisis inicial de resultados.  

4. **Automatización del flujo y aplicación a las 3 regiones**  
   - Definición de funciones para cargar datos, entrenar, validar y obtener métricas.  
   - Ejecución de los pasos previos en las tres regiones.  

5. **Preparación para cálculo de ganancias**  
   - Almacenamiento de variables necesarias para el cálculo económico.  
   - Comparación del punto de equilibrio (111.1 unidades por pozo) con la media de reservas por región.  
   - Conclusiones preliminares de viabilidad.  

6. **Selección de pozos top-200 por región**  
   - Seleccionar los 200 pozos con mayores predicciones en cada región.  
   - Calcular el volumen total estimado y el beneficio esperado.  

7. **Cálculo de beneficio por región**  
   - Función para estimar la ganancia total de los pozos seleccionados.  
   - Comparación de beneficios entre regiones.  
   - Identificación preliminar de la mejor región.  

8. **Bootstrapping (1000 iteraciones)**  
   - Aplicación de la técnica de remuestreo sobre las predicciones top-200.  
   - Cálculo de beneficio promedio, intervalo de confianza al 95% y riesgo de pérdida.  
   - Comparación de regiones considerando beneficio esperado y riesgo < 2.5%.  

9. **Conclusiones y recomendación final**  
   - Resumen de resultados obtenidos en todas las etapas.  
   - Recomendación de la región óptima para invertir.  
   - Validación de si coincide con la elección preliminar.  

---

### ⚙️ Pasos previstos para `src/`

* **`data_loading.py`**

  * Funciones para cargar datasets de cada región.
* **`modeling.py`**

  * Función para entrenar regresión lineal y evaluar métricas.
* **`economics.py`**

  * Función para calcular beneficio esperado a partir de predicciones.
* **`bootstrap.py`**

  * Función para aplicar bootstrapping y obtener distribución de beneficios.

---

## ⚙️ Estructura del proyecto

```bash
.
├── datasets/
│   └── geo_data_0.csv       # Datos región 0
│   └── geo_data_1.csv       # Datos región 1
│   └── geo_data_2.csv       # Datos región 2
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_modelado_validacion.ipynb
│   └── 03_beneficio_bootstrap.ipynb
├── src/
│   ├── data_loading.py
│   ├── modeling.py
│   ├── economics.py
│   └── bootstrap.py
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

(Se completará al final del proyecto con base en resultados reales).

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
