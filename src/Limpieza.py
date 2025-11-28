# src/funcion.py

import os
import pandas as pd


def limpiar_dataset(ruta_entrada: str, ruta_salida: str) -> pd.DataFrame:
    """
    Carga el dataset original, aplica un proceso de limpieza y guarda
    un dataset limpio en la ruta indicada.

    Parámetros
    ----------
    ruta_entrada : str
        Ruta al archivo CSV original.
    ruta_salida : str
        Ruta donde se guardará el CSV limpio.
    verbose : bool
        Si es True, muestra información por pantalla sobre el proceso.

    Retorna
    -------
    df : pandas.DataFrame
        DataFrame limpio listo para su análisis.
    """

    # Carga del dataset crudo
    df = pd.read_csv(ruta_entrada)
    print("Dimensiones iniciales del dataset crudo:", df.shape)

    # =============================
    # 1. Conversión de tipos
    # =============================
    sales_cols = ["na_sales", "pal_sales", "jp_sales", "other_sales", "total_sales"]

    for col in sales_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df["last_update"] = pd.to_datetime(df["last_update"], errors="coerce")
    df["critic_score"] = pd.to_numeric(df["critic_score"], errors="coerce")


    print("\nTipos de datos tras conversión inicial:")
    print(df.dtypes)

    # =============================
    # 2. Tratamiento de valores nulos
    # =============================

    # 2.1 Eliminar filas sin ventas globales
    antes_filtrado_sales = len(df)
    df = df.dropna(subset=["total_sales"])
    despues_filtrado_sales = len(df)


    print("\nFilas eliminadas por total_sales nulo:", antes_filtrado_sales - despues_filtrado_sales)

    # 2.2 Rellenar nulos en columnas categóricas
    df["developer"] = df["developer"].fillna("Unknown")
    df["publisher"] = df["publisher"].fillna("Unknown")

    # 2.3 Rellenar nulos en critic_score con la mediana
    df["critic_score"] = df["critic_score"].fillna(df["critic_score"].median())

    # 2.4 Rellenar nulos en ventas regionales con 0
    df[["na_sales", "pal_sales", "jp_sales", "other_sales"]] = (
        df[["na_sales", "pal_sales", "jp_sales", "other_sales"]].fillna(0)
    )

    # =============================
    # 3. Recalcular total_sales y eliminar incoherencias
    # =============================

    df["total_sales_recalc"] = df[["na_sales", "pal_sales", "jp_sales", "other_sales"]].sum(axis=1)

    diferentes = (df["total_sales"] != df["total_sales_recalc"]).sum()

    print("Filas donde total_sales original difiere de la suma de regiones:", diferentes)

    df["total_sales"] = df["total_sales_recalc"]
    df = df.drop(columns=["total_sales_recalc"])

    # Eliminar ventas negativas
    condicion_ventas = (
        (df["total_sales"] >= 0)
        & (df["na_sales"] >= 0)
        & (df["pal_sales"] >= 0)
        & (df["jp_sales"] >= 0)
        & (df["other_sales"] >= 0)
    )
    df = df[condicion_ventas]

    # Puntuaciones negativas
    df = df[df["critic_score"] >= 0]

    # =============================
    # 4. Eliminación de duplicados
    # =============================

    antes = len(df)
    df = df.drop_duplicates()
    despues = len(df)
    print("Duplicados eliminados:", antes - despues)

    # 5. Normalización de categorías

    df["genre"] = df["genre"].astype(str).str.strip().str.lower()
    df["console"] = df["console"].astype(str).str.strip().str.upper()
    df["publisher"] = df["publisher"].astype(str).str.strip().str.title()
    df["developer"] = df["developer"].astype(str).str.strip().str.title()

    # 6. Comprobación final de calidad
    
    print("\nResumen final de valores nulos:")
    print(df.isna().sum())

    print("\nTipos de datos después de la limpieza:")
    print(df.dtypes)

    print("\nDimensiones finales del dataset limpio:", df.shape)
        
    # 7. Guardado del dataset limpio

    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    df.to_csv(ruta_salida, index=False)


    return df
