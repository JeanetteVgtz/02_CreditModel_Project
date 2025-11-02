# 02_CreditModel_Project

### Asignatura:
**Modelos de Crédito**

### Presentado por:
- **Jeanette Valenzuela Gutiérrez**  
- **Paulina Elizabeth Mejía Hori**

**Profesor:** Rodolfo Slay Ramos  
**ITESO — Tlaquepaque, Jal.**  
**Octubre 2025**

---

## Descripción General

Este proyecto desarrolla un **modelo integral de riesgo de crédito y formación de tasas de interés personalizadas**, enfocado en productos de **tarjetas de crédito**.  
El sistema utiliza técnicas de **Machine Learning supervisado** para estimar la **Probabilidad de Incumplimiento (PD)** de cada cliente y combina estos resultados con componentes financieros para calcular una **tasa final ajustada al riesgo individual**.

El objetivo es **automatizar la evaluación crediticia** y asignar condiciones de crédito proporcionales al perfil del cliente, maximizando la rentabilidad y minimizando la pérdida esperada.

---

## Estructura del Repositorio
02_CreditModel_Project/
│
├── .ipynb_checkpoints/ # Archivos temporales del notebook
├── .venv/ # Entorno virtual de desarrollo
│
├── LICENSE # Licencia del proyecto
├── PROYECTO MODELO DE CRÉDITO.pdf # Reporte final del modelo (entrega académica)
├── README.md # Archivo de documentación principal
├── VISUALS.xlsx # Visualizaciones y tablas de resultados
├── nueva_solicitud_formato.xlsx # Plantilla editable para nuevos clientes
├── proyecto_creditmodel.ipynb # Notebook principal del modelo
├── requirements.txt # Dependencias del proyecto
└── train.csv # Dataset original para entrenamiento


💡 Se recomienda usar un entorno virtual (`python -m venv .venv`) o `conda` para mantener las dependencias aisladas.

---

## 🚀 Flujo del Modelo

### Preparación y Limpieza de Datos
- Carga del dataset `train.csv`.
- Eliminación de variables irrelevantes.
- Codificación de variables categóricas.
- Creación de variable objetivo binaria (default / no default).

---

### Análisis Exploratorio (EDA)
- Análisis de distribuciones de score, edad, ingresos y tasas.  
- Cálculo de correlaciones entre variables clave.  
- Identificación de factores determinantes del riesgo crediticio.  
- Resultados visuales disponibles en `VISUALS.xlsx`.

---

### Entrenamiento y Validación
Modelos comparativos:
- **Regresión Logística:** modelo lineal base interpretativo.  
- **Random Forest:** modelo no lineal con mayor precisión.

Se aplicó:
- **Validación cruzada estratificada (Stratified K-Fold)**  
- **Búsqueda aleatoria de hiperparámetros (RandomizedSearchCV)**  

**Resultados:**
- AUC final (Random Forest optimizado): **0.945**  
- AUC base (Regresión Logística): **0.809**

---

### Cálculo de Parámetros de Riesgo
- **PD (Probability of Default):** probabilidad de incumplimiento.  
- **LGD (Loss Given Default):** 65% (créditos sin garantía).  
- **EAD (Exposure at Default):** exposición total al riesgo.  

---

### Formación de la Tasa de Interés

La tasa final se calcula mediante la fórmula:

**r_final = r_base + (PD × LGD × k)**

**Donde:**
- r_base = 20.5%  
- LGD = 65%  
- k = 1.5 (multiplicador de riesgo)

| Componente | Descripción | Valor |
|-------------|-------------|--------|
| Tasa de referencia | Tasa base o de fondeo | 7.5% |
| Prima por inflación | Compensa pérdida de poder adquisitivo | 3.76% |
| Prima por liquidez | Ajuste por disponibilidad de recursos | 2.0% |
| Costos operativos | Gastos administrativos y cobranza | 3.5% |
| Margen de beneficio | Rentabilidad mínima esperada | 3.0% |

---

### Segmentación por Nivel de Riesgo

| Nivel | Descripción | Rango de Tasa | Condición |
|-------|--------------|---------------|------------|
| Tier 1 | Excelente | < 35% | Bajo riesgo — tasa competitiva |
| Tier 2 | Bueno | 35–45% | Riesgo medio-bajo |
| Tier 3 | Regular | 45–60% | Riesgo moderado |
| Tier 4 | Alto Riesgo | > 60% | Riesgo elevado |

---

### Evaluación Automática de Nuevos Clientes

El archivo `nueva_solicitud_formato.xlsx` permite ingresar los datos de un nuevo solicitante.  
El sistema genera automáticamente:

- PD estimada  
- Tasa personalizada  
- Nivel de riesgo (Tier)  
- Decisión final (**Aprobado** / **Rechazado**)  

**Ejemplo de salida (archivo `resultado_nuevo_cliente.xlsx`):**

| Cliente | PD (%) | Tasa (%) | Nivel | Decisión |
|----------|--------|----------|--------|-----------|
| 1 | 24.5 | 43.6 | Tier 3 - Regular | Aprobado |
| 2 | 25.5 | 44.6 | Tier 3 - Regular | Aprobado |
| 3 | 43.0 | 61.7 | Tier 4 - Alto Riesgo | Aprobado |

---

## Resultados Principales

- **Modelo final:** Random Forest Optimizado  
- **AUC-ROC:** 0.945  
- **Precisión promedio:** 89%  
- **Rango de tasas:** 20% – 120%  
- **Automatización:** 100% del flujo de evaluación y pricing  

---

## Conclusiones

El modelo integra análisis de riesgo, componentes financieros y automatización de decisiones, permitiendo **alinear el riesgo crediticio con la rentabilidad esperada**.  

**Principales aprendizajes:**  
Durante el desarrollo, se intentó utilizar datasets alternativos, pero muchos carecían de variables suficientes para un entrenamiento confiable.  
También fue necesario calibrar cuidadosamente las tasas, ya que inicialmente el modelo aprobaba o rechazaba sin coherencia.  
Finalmente, se consiguió una automatización sólida que **evalúa nuevas solicitudes en tiempo real**, asignando tasas proporcionales al riesgo real del cliente.

---

## Autoras

| Nombre | Rol | Contacto |
|--------|------|----------|
| **Jeanette Valenzuela Gutiérrez** | Desarrollo técnico, modelado y pricing | [GitHub @JeanetteVgtz](https://github.com/JeanetteVgtz) |
| **Paulina Elizabeth Mejía Hori** | Análisis financiero y documentación | — |

---

## Licencia

Este proyecto se distribuye bajo la licencia **MIT**.  
Consulta el archivo [LICENSE](./LICENSE) para más detalles.


