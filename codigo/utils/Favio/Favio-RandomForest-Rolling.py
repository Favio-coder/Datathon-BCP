import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


train = pd.read_csv("data/raw/train.csv")

features = [
    "banda_riesgo",
    "numero_productos",
    "activo_movil",
    "tiene_tarjeta_credito",
    "dias_ultima_transaccion",
]

target = "objetivo"

categoricas = ["banda_riesgo"]

numericas = [
    "numero_productos",
    "dias_ultima_transaccion",
]

booleanas = [
    "activo_movil",
    "tiene_tarjeta_credito",
]


def crear_modelo():

    preprocesamiento = ColumnTransformer(
        transformers=[
            (
                "categoricas",
                OneHotEncoder(handle_unknown="ignore"),
                categoricas,
            ),
            (
                "numericas",
                "passthrough",
                numericas,
            ),
            (
                "booleanas",
                "passthrough",
                booleanas,
            ),
        ]
    )

    modelo = RandomForestClassifier(
        n_estimators=300,
        max_depth=8,
        min_samples_leaf=50,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced",
    )

    pipeline = Pipeline(
        steps=[
            ("preprocesamiento", preprocesamiento),
            ("modelo", modelo),
        ]
    )

    return pipeline


periodos = [
    (202608, 202609),  # Enero-Agosto → Septiembre
    (202609, 202610),  # Enero-Septiembre → Octubre
    (202610, 202611),  # Enero-Octubre → Noviembre
]


resultados = []


for ultimo_mes_train, mes_validacion in periodos:

    print("\n" + "=" * 50)
    print(f"Entrenamiento hasta: {ultimo_mes_train}")
    print(f"Validación: {mes_validacion}")
    print("=" * 50)

    train_model = train[
        train["mes"] <= ultimo_mes_train
    ].copy()

    validacion = train[
        train["mes"] == mes_validacion
    ].copy()

    X_train = train_model[features]
    y_train = train_model[target]

    X_valid = validacion[features]
    y_valid = validacion[target]

    print(f"Filas entrenamiento: {len(train_model):,}")
    print(f"Filas validación:    {len(validacion):,}")

    # Crear modelo nuevo para cada período
    pipeline = crear_modelo()

    print("Entrenando...")

    pipeline.fit(X_train, y_train)

    probabilidades = pipeline.predict_proba(X_valid)[:, 1]

    auc = roc_auc_score(
        y_valid,
        probabilidades
    )

    gini = 2 * auc - 1

    print(f"AUC:  {auc:.6f}")
    print(f"Gini: {gini:.6f}")

    resultados.append({
        "train_hasta": ultimo_mes_train,
        "validacion": mes_validacion,
        "auc": auc,
        "gini": gini,
    })

resultados_df = pd.DataFrame(resultados)

print("\n")
print("=" * 50)
print("RESUMEN VALIDACIÓN ROLLING")
print("=" * 50)

print(
    resultados_df.to_string(
        index=False,
        float_format=lambda x: f"{x:.6f}"
    )
)

print("\nPromedio AUC:", resultados_df["auc"].mean())
print("Promedio Gini:", resultados_df["gini"].mean())

print("Desviación AUC:", resultados_df["auc"].std())
print("Desviación Gini:", resultados_df["gini"].std())