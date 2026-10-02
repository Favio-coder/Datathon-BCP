# Análisis exploratorio inicial

## 1. Tasa de conversión por mes

La tasa de conversión se mantiene relativamente estable durante el período de entrenamiento, aproximadamente entre **14% y 16%**.

Observaciones:

* Enero: **14.65%**
* Febrero: **15.75%** → máximo observado
* Marzo: **14.90%**
* Abril: **15.30%**
* Mayo: **15.60%**
* Junio: **15.50%**
* Los meses restantes mantienen valores dentro de un rango similar.

### Interpretación

No se observa un cambio temporal extremo en la tasa de conversión. Por lo tanto, el comportamiento del objetivo parece relativamente estable entre meses.

Sin embargo, la validación debe seguir siendo temporal porque el conjunto de prueba corresponde exclusivamente a diciembre de 2026.

---

## 2. Activo móvil

La variable `activo_movil` muestra una diferencia apreciable:

* `True`: aproximadamente **16%** de conversión.
* `False`: aproximadamente **13%** de conversión.

### Interpretación

Los clientes activos en la aplicación móvil presentan una mayor tasa de conversión en el conjunto analizado.

Esto indica que `activo_movil` contiene señal predictiva y debe mantenerse como variable candidata para los modelos.

---

## 3. Tarjeta de crédito

La variable `tiene_tarjeta_credito` presenta una diferencia menor:

* `True`: aproximadamente **15%** de conversión.
* `False`: aproximadamente **14%** de conversión.

### Interpretación

Existe una diferencia entre ambos grupos, aunque parece ser menor que la observada para `activo_movil`.

Se mantiene como variable candidata, pero posteriormente debemos comprobar mediante validación si realmente mejora el AUC.

---

## 4. Número de productos

Se observa una tendencia positiva: **a mayor número de productos bancarios, mayor tasa de conversión**.

### Interpretación

`numero_productos` parece contener una relación útil con el objetivo. Esto coincide con el análisis inicial, donde presentó una señal superior a la de varias variables aparentemente irrelevantes.

Debe mantenerse como variable candidata y evaluarse mediante modelos.

---

## 5. Variables candidatas actuales

A partir del análisis exploratorio, las principales variables candidatas son:

```text
banda_riesgo
numero_productos
activo_movil
tiene_tarjeta_credito
dias_ultima_transaccion
```

Estas cinco variables presentan evidencia inicial de relación con `objetivo`.

Las variables:

```text
antiguedad_direccion_meses
visitas_web_ultimos_90_dias
distancia_sucursal_km
dia_preferido_pago
```

se mantendrán como variables experimentales para comprobar si aportan información adicional.

`dias_ultima_interaccion` se excluye inicialmente debido al covariate shift identificado entre entrenamiento y diciembre.

---

## 6. Baseline actual

Se entrenó una primera `LogisticRegression` utilizando las cinco variables principales.

Validación temporal:

```text
Entrenamiento: enero 2026 → octubre 2026
Validación: noviembre 2026
```

Resultado:

```text
AUC:  0.598115
Gini: 0.196230
```

Este resultado constituye nuestro **baseline inicial**.

---

## 7. Próximo paso

Crear random forest o random tree, or decision tree
