# BCP Datathon 🚀

Repositorio del equipo para el desarrollo de nuestra solución para la BCP Datathon.

El repositorio está organizado para permitir que los 5 integrantes trabajen de manera independiente en diferentes modelos, manteniendo una estructura común para la evaluación, comparación y selección de resultados.

---

## Estructura del repositorio

```text
BCP_Datathon/
│
├── codigo/
│   │
│   ├── evaluation/
│   │   └── # Evaluación y comparación de los modelos
│   │
│   ├── modelos/
│   │   ├── modelo_Apellido1.ipynb
│   │   ├── modelo_Apellido2.ipynb
│   │   ├── modelo_Apellido3.ipynb
│   │   ├── modelo_Apellido4.ipynb
│   │   └── modelo_Apellido5.ipynb
│   │
│   └── utils/
│       └── # Funciones y utilidades compartidas
│
├── data/
│   └── # Datos utilizados para el proyecto
│
├── resultados/
│   ├── # Métricas
│   ├── # Predicciones
│   └── # Gráficos y resultados finales
│
├── DATASET_DESCRIPTION.md
└── Readme.md
```

## Organización de los modelos
Cada integrante tendrá un notebook propio dentro de:
Cada integrante tendrá un notebook propio dentro de:

codigo/modelos/

El nombre del archivo debe seguir obligatoriamente este formato:

modelo_APELLIDO.ipynb

Por ejemplo:

codigo/modelos/
├── modelo01_Asturimac.ipynb
├── modelo01_Jayo.ipynb
├── modelo02_Asturimac.ipynb

Esto permite identificar rápidamente qué integrante desarrolló cada experimento

Nota: en caso mejores un modelo o agregue un nuevo modelo debes versionarlo 

## Contenido obligatorio de cada modelo
Cada notebook debe estar organizado de manera similar

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

Al inicio del notebook se recomienda colocar:
# Modelo: XGBoost
# Autor: Apellido

# Evaluación
Los modelos serán evaluados utilizando una metodología común.

Los resultados de cada modelo deberán registrarse en:

codigo/evaluation/

Aquí se realizará la comparación entre los diferentes modelos desarrollados por el equipo.

Ejemplo:

codigo/evaluation/
├── comparacion_modelos.ipynb
└── ...

La comparación deberá considerar la métrica oficial utilizada por la Datathon: **ROC AUC**.

Cada integrante puede calcular y reportar otras métricas (F1, precision, recall, accuracy, log loss, etc.) para tener un análisis más completo del comportamiento de su modelo. Sin embargo, **la métrica decisiva es ROC AUC**, ya que es la única que permite comparar y elegir el modelo final.

Por lo tanto, la tabla comparativa siempre debe incluir la columna de ROC AUC. Las demás métricas son opcionales y complementarias.

Ejemplo:

Modelo	Integrante	ROC AUC	F1	Accuracy
Random Forest	Asturimac	0.81	0.79	0.83
XGBoost	Jayo	0.85	0.82	0.86
LightGBM	Rojas	0.83	0.78	0.84

Los valores anteriores son únicamente un ejemplo. **ROC AUC es la columna de referencia para la comparación y la selección del modelo final.**

lujo de trabajo

El flujo general del proyecto será:

              DATASET
                 │
                 ▼
        Exploración del dataset
                 │
                 ▼
          Preprocesamiento
                 │
                 ▼
        ┌────────┼────────┐
        │        │        │
        ▼        ▼        ▼
     Modelo 1 Modelo 2 Modelo 3
        │        │        │
        ▼        ▼        ▼
     Modelo 4 Modelo 5
        │        │
        └────┬───┘
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
📌 Reglas importantes
1. No modificar los datos originales

Los archivos originales dentro de data/ deben conservarse sin modificaciones.

Si un integrante necesita transformar los datos, debe guardar el resultado correspondiente y documentar qué transformación realizó.

2. Cada integrante trabaja en su propio modelo

No modificar el notebook de otro integrante sin coordinación.

Ejemplo:

modelo_Asturimac.ipynb
modelo_Jayo.ipynb
modelo_Rojas.ipynb
modelo_Perez.ipynb
modelo_Garcia.ipynb

Cada persona es responsable de mantener actualizado su notebook.

3. ROC AUC es la métrica principal

Los resultados solamente pueden compararse correctamente si utilizamos la misma métrica y metodología de evaluación.

La métrica principal y obligatoria de comparación es el **ROC AUC**. Cualquier otra métrica (F1, precision, recall, accuracy, log loss, etc.) puede reportarse adicionalmente para complementar el análisis, pero no debe usarse para decidir cuál modelo es mejor.

Regla práctica: si dos modelos no tienen ROC AUC comparable, no se pueden comparar.

4. Registrar los experimentos

Cada integrante debe indicar dentro de su notebook:

Algoritmo utilizado.
Variables utilizadas.
Preprocesamiento realizado.
Feature Engineering.
Hiperparámetros.
Métrica obtenida.
Observaciones.
Conclusiones.
🌿 Git y ramas

Cada integrante debe trabajar utilizando su propia rama.

Formato recomendado:

feature/modelo-apellido

Ejemplo:

git checkout -b feature/modelo-asturimac

Otro integrante:

git checkout -b feature/modelo-jayo
🔀 Flujo de Git

El flujo recomendado es:

                 main
                   │
                   ▼
                develop
             /     |     \
            /      |      \
           ▼       ▼       ▼
       modelo-1 modelo-2 modelo-3
           │       │       │
           ▼       ▼       ▼
       Pull Request
             │
             ▼
          develop
             │
             ▼
            main
Antes de comenzar a trabajar
git checkout develop
git pull origin develop

Crear una rama:

git checkout -b feature/modelo-apellido
💾 Commits

Los commits deben describir claramente qué se realizó.

Ejemplos
git add .
git commit -m "feat: agrega modelo XGBoost"
git commit -m "feat: agrega feature engineering"
git commit -m "fix: corrige preprocesamiento"
git commit -m "docs: actualiza resultados del modelo"
📈 Resultados

Los resultados importantes de los modelos deberán almacenarse en:

resultados/

Por ejemplo:

resultados/
├── metricas.csv
├── predicciones/
└── graficos/

Las predicciones generadas por cada modelo deben identificarse claramente.

Ejemplo:

resultados/predicciones/
├── predicciones_Asturimac.csv
├── predicciones_Jayo.csv
├── predicciones_Rojas.csv
├── predicciones_Perez.csv
└── predicciones_Garcia.csv
🏆 Selección del modelo final

Una vez que todos los integrantes hayan desarrollado y evaluado sus modelos:

Modelo 1 ──┐
Modelo 2 ──┤
Modelo 3 ──┼──► Comparación ──► Análisis ──► Modelo final
Modelo 4 ──┤
Modelo 5 ──┘

El equipo analizará los resultados obtenidos y decidirá qué configuración utilizar para generar la predicción final.

También se podrá evaluar la combinación de varios modelos mediante técnicas como:

Voting
Blending
Stacking
Ensemble

si los resultados experimentales justifican su utilización.

🚨 Importante

No se debe asumir que un modelo es mejor únicamente porque obtuvo un resultado superior en un experimento aislado.

Antes de seleccionar el modelo final se debe verificar:

Misma metodología de evaluación.
Misma métrica.
Ausencia de data leakage.
Reproducibilidad.
Rendimiento en validación.
Configuración utilizada.
Estabilidad del resultado.
🎯 Objetivo del repositorio

El objetivo no es simplemente tener cinco algoritmos diferentes.

El objetivo es construir un proceso reproducible:

DATOS
  ↓
ANÁLISIS
  ↓
PREPROCESAMIENTO
  ↓
EXPERIMENTACIÓN
  ↓
MODELOS
  ↓
EVALUACIÓN
  ↓
COMPARACIÓN
  ↓
MODELO FINAL
  ↓
SUBMISSION

Cada integrante puede experimentar libremente dentro de su modelo, pero todos debemos mantener una metodología común para poder comparar los resultados.

🚀 Regla principal

Cada integrante experimenta por separado, pero todos evaluamos bajo las mismas reglas.


### Una mejora que te recomiendo para su equipo

Yo **no pondría el apellido solamente en el notebook**, sino también en la rama y en los archivos de resultados. Así, cuando estén trabajando los 5 simultáneamente, todo queda identificable:

```text
codigo/
├── evaluation/
├── modelos/
│   ├── modelo_Asturimac.ipynb
│   ├── modelo_Jayo.ipynb
│   ├── modelo_Rojas.ipynb
│   ├── modelo_Perez.ipynb
│   └── modelo_Garcia.ipynb
└── utils/

resultados/
├── predicciones/
│   ├── predicciones_Asturimac.csv
│   ├── predicciones_Jayo.csv
│   └── ...
└── metricas.csv

Y las ramas:

feature/modelo-asturimac
feature/modelo-jayo
feature/modelo-rojas
feature/modelo-perez
feature/modelo-garcia

Así, nadie toca el notebook de otro y el historial de Git queda clarísimo.