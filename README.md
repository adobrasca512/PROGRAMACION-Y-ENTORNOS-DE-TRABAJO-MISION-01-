# Proyecto IA — Clasificador de flores - Cambio 2 realizado en la misma linea

Prototipo de clasificación con el dataset Iris integrado en scikit-learn. Se utiliza para practicar Git/GitHub, no para evaluar calidad predictiva.

## Instalación

```bash
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

```

Recuerda que ára usar esto necesitas una version de python avanzada

## Ejecución

```bash
python -m src.predictor
python -m unittest discover -s tests -v
```

## Estructura

- `src/predictor.py`: entrenamiento mínimo y predicción.
- `src/metricas.py`: funciones auxiliares para ampliar. Aqui se añadio la funcion: calcular_precision que se encarga de calcular el porcentaje de predicciones que acierta el modelo. Con el calculo de aciertos/total. En la funcion llama a contar_aciertos y el valor retornado se le calcula la precisión con la formula mencionada anteriormente.
- `tests/`: pruebas de partida.

## Colaboración

Usad ramas `feature/*`, Pull Requests y revisiones de compañeros.
