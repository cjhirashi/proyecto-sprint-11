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
