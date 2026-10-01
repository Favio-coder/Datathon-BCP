# 🚀 BCP Datathon

Repositorio del equipo para el desarrollo de nuestra solución para la **BCP Datathon**.

El repositorio está organizado para que los 5 integrantes trabajen de manera independiente en diferentes modelos, manteniendo una estructura común para la **evaluación**, **comparación** y **selección** de resultados.

---

## 📁 Estructura del repositorio

```text
BCP_Datathon/
├── codigo/
│   ├── evaluation/            # Evaluación y comparación de los modelos
│   ├── modelos/               # Un notebook por integrante
│   │   ├── modelo_Asturimac.ipynb
│   │   ├── modelo_Jayo.ipynb
│   │   ├── modelo_Rojas.ipynb
│   │   ├── modelo_Perez.ipynb
│   │   └── modelo_Garcia.ipynb
│   └── utils/                 # Funciones y utilidades compartidas
│
├── data/                      # Datos utilizados (NO se modifican)
│
├── resultados/                # Métricas, predicciones y gráficos
│   ├── metricas.csv
│   ├── predicciones/
│   └── graficos/
│
├── DATASET_DESCRIPTION.md
└── Readme.md
```

---

## 👥 Organización de los modelos

Cada integrante tiene su propio notebook dentro de `codigo/modelos/`.

El nombre del archivo debe seguir **obligatoriamente** este formato:

```text
modelo_APELLIDO.ipynb
```

Esto permite identificar rápidamente qué integrante desarrolló cada experimento.

> **Nota:** si mejoras un modelo o agregas uno nuevo, debes versionarlo.

---

## 📓 Contenido obligatorio de cada notebook

Cada notebook debe seguir esta estructura, en orden:

1. Importación de librerías
2. Carga de datos
3. Preprocesamiento
4. Feature Engineering
5. División de datos
6. Entrenamiento del modelo
7. Predicciones
8. Evaluación
9. Resultados
10. Conclusiones

Se recomienda colocar una cabecera al inicio del notebook:

```python
# Modelo: XGBoost
# Autor: Apellido
```

---

## 📊 Evaluación

Los modelos se evalúan con una **metodología común** para que los resultados sean comparables.

### Métricas

| Métrica | Rol | Obligatoria |
| :--- | :--- | :---: |
| **ROC AUC** | Métrica oficial de la Datathon. Define cuál modelo es mejor. | ✅ Sí |
| F1, Precision, Recall, Accuracy | Análisis complementario del comportamiento del modelo. | ➖ Opcional |
| Log Loss, KS, Lift | Diagnóstico de calibración y del poder de discriminar. | ➖ Opcional |

> **Regla:** cada integrante puede reportar las métricas que considere útiles, pero **la única métrica válida para comparar y elegir el modelo final es el ROC AUC**.

Si dos modelos no reportan ROC AUC bajo la misma metodología, **no son comparables**.

### Registro de resultados

Los resultados de cada modelo se registran en `codigo/evaluation/`, donde se realiza la comparación entre los modelos del equipo:

```text
codigo/evaluation/
├── comparacion_modelos.ipynb
└── ...
```

### Formato de la tabla comparativa

La columna **ROC AUC** es obligatoria; las demás son opcionales.

| Modelo | Integrante | ROC AUC | F1 | Accuracy |
| :--- | :--- | ---: | ---: | ---: |
| Random Forest | Asturimac | 0.81 | 0.79 | 0.83 |
| XGBoost | Jayo | **0.85** | 0.82 | 0.86 |
| LightGBM | Rojas | 0.83 | 0.78 | 0.84 |

> Los valores son únicamente un ejemplo. **El modelo ganador es el de mayor ROC AUC.**

---

## 🔄 Flujo de trabajo

```text
                      DATASET
                         │
                         ▼
              Exploración del dataset
                         │
                         ▼
                 Preprocesamiento
                         │
                         ▼
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
    Modelo 1         Modelo 2         Modelo 3
        │                │                │
        ▼                ▼                ▼
    Modelo 4         Modelo 5
        │                │
        └────────┬───────┘
                 ▼
            EVALUACIÓN
                 │
                 ▼
      COMPARACIÓN DE MODELOS
                 │
                 ▼
         MEJORES RESULTADOS
                 │
                 ▼
           MODELO FINAL
                 │
                 ▼
          PREDICCIÓN TEST
                 │
                 ▼
         SUBMISSION FINAL
```

---

## 📌 Reglas importantes

### 1. No modificar los datos originales

Los archivos dentro de `data/` se conservan sin modificaciones.

Si necesitas transformar los datos, guarda el resultado aparte y documenta qué transformación hiciste.

### 2. Cada integrante trabaja en su propio modelo

No modifiques el notebook de otro integrante sin coordinación. Cada persona es responsable de mantener actualizado su notebook.

### 3. ROC AUC es la métrica principal

Los resultados solo son comparables si usamos la misma métrica y metodología.

- **ROC AUC** es obligatoria y define el orden de los modelos.
- Cualquier otra métrica es informativa, no decisiva.

### 4. Registrar los experimentos

Cada notebook debe indicar:

- Algoritmo utilizado
- Variables utilizadas
- Preprocesamiento realizado
- Feature Engineering
- Hiperparámetros
- **ROC AUC obtenido**
- Observaciones
- Conclusiones

---

## 🌿 Git y ramas

Cada integrante trabaja en su propia rama con el formato:

```text
feature/modelo-apellido
```

```bash
git checkout -b feature/modelo-asturimac
```

Otro integrante:

```bash
git checkout -b feature/modelo-jayo
```

### Flujo de Git

```text
              main
                │
                ▼
             develop
            /   |   \
           ▼    ▼    ▼
     modelo-1  modelo-2  modelo-3
           ▼    ▼    ▼
        Pull Request
              │
              ▼
           develop
              │
              ▼
             main
```

Antes de comenzar a trabajar:

```bash
git checkout develop
git pull origin develop
git checkout -b feature/modelo-apellido
```

### Commits

Los commits deben describir claramente qué se realizó:

```bash
git add .
git commit -m "feat: agrega modelo XGBoost"
git commit -m "feat: agrega feature engineering"
git commit -m "fix: corrige preprocesamiento"
git commit -m "docs: actualiza resultados del modelo"
```

---

## 📈 Resultados

Los resultados importantes se almacenan en `resultados/`:

```text
resultados/
├── metricas.csv
├── predicciones/
│   ├── predicciones_Asturimac.csv
│   ├── predicciones_Jayo.csv
│   ├── predicciones_Rojas.csv
│   ├── predicciones_Perez.csv
│   └── predicciones_Garcia.csv
└── graficos/
```

Cada predicción debe identificarse claramente con el nombre de su autor.

---

## 🏆 Selección del modelo final

```text
Modelo 1 ──┐
Modelo 2 ──┤
Modelo 3 ──┼──► Comparación ──► Análisis ──► Modelo final
Modelo 4 ──┤
Modelo 5 ──┘
```

El equipo analizará los resultados y decidirá qué configuración usar para la predicción final, **priorizando el modelo con mayor ROC AUC**.

También se puede evaluar la combinación de varios modelos mediante:

- Voting
- Blending
- Stacking
- Ensemble

…si los resultados experimentales lo justifican.

### Antes de elegir, verifica

- [ ] Misma metodología de evaluación
- [ ] ROC AUC reportado y comparable
- [ ] Ausencia de data leakage
- [ ] Reproducibilidad
- [ ] Rendimiento en validación
- [ ] Configuración documentada
- [ ] Estabilidad del resultado

> 🚨 No asumas que un modelo es mejor solo porque obtuvo un resultado superior en un experimento aislado.

---

## 🎯 Objetivo del repositorio

El objetivo no es simplemente tener cinco algoritmos diferentes, sino construir un proceso reproducible:

```text
DATOS → ANÁLISIS → PREPROCESAMIENTO → EXPERIMENTACIÓN
      → MODELOS → EVALUACIÓN → COMPARACIÓN
      → MODELO FINAL → SUBMISSION
```

Cada integrante puede experimentar libremente dentro de su modelo, pero todos mantenemos una metodología común para poder comparar los resultados.

> ### 🚀 Regla principal
>
> **Cada integrante experimenta por separado, pero todos evaluamos bajo las mismas reglas: misma metodología y mismo ROC AUC.**
