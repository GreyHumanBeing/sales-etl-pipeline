import pandas as pd

def extraer_datos(path):
    """
    Carga un archivo CSV y devuelve un DataFrame.

    Args:
        path (str): Ruta del archivo CSV.

    Returns:
        pandas.DataFrame: Datos cargados desde el archivo.
    """
    df = pd.read_csv(path)

    return df
