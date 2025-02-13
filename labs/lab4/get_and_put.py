import pandas as pd
import random

def merge_csv(csv1_path, csv2_path, columns_csv1, columns_csv2, output_filename):
    # Leer los archivos CSV
    df1 = pd.read_csv(csv1_path)
    df2 = pd.read_csv(csv2_path)
    
    # Seleccionar las columnas indicadas
    df1_selected = df1[columns_csv1]
    df2_selected = df2[columns_csv2]
    
    # Ajustar los tamaños de los DataFrames
    max_rows = max(len(df1_selected), len(df2_selected))
    
    # Rellenar datos si un DataFrame tiene menos filas que el otro
    for col in df1_selected.columns:
        while len(df1_selected) < max_rows:
            df1_selected = pd.concat([df1_selected, df1_selected.sample(n=1)], ignore_index=True)
    
    for col in df2_selected.columns:
        while len(df2_selected) < max_rows:
            df2_selected = pd.concat([df2_selected, df2_selected.sample(n=1)], ignore_index=True)
    
    # Convertir a enteros si los datos lo permiten
    df1_selected = df1_selected.map(lambda x: int(x) if isinstance(x, float) and x.is_integer() else x)
    df2_selected = df2_selected.map(lambda x: int(x) if isinstance(x, float) and x.is_integer() else x)
    
    # Unir los DataFrames lado a lado
    merged_df = pd.concat([df1_selected, df2_selected], axis=1)
    
    # Guardar el resultado en un nuevo archivo CSV
    merged_df.to_csv(output_filename, index=False)
    print(f"Archivo guardado como: {output_filename}")

csv1 = "./Productos.csv"
csv2 = "./ubicaciones.csv"
columnas_csv1 = ["productID"]
columnas_csv2 = ["ubicacionID"]
output_file = "is_in.csv"

merge_csv(csv1, csv2, columnas_csv1, columnas_csv2, output_file)