def cargar_datos(df, path):
    """
    Guarda un DataFrame en un archivo CSV.

    Args:
        df (pandas.DataFrame): DataFrame que se desea guardar.
        path (str): Ruta donde se guardará el archivo.

    Returns:
        None
    """

    df.to_csv(path, index=False)