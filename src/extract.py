import pandas as pd
from src.logger import retornar_logger


logger = retornar_logger("extract.py")


def extraer_datos(path):
    """
    Carga un archivo CSV y devuelve un DataFrame.

    Args:
        path (str): Ruta del archivo CSV.

    Returns:
        pandas.DataFrame: Datos cargados desde el archivo.
    """
    try:
        df = pd.read_csv(path)
        logger.info(f"Archivo leído correctamente desde {path}: {len(df)} filas")
        return df

    except FileNotFoundError as e:
        logger.error(f"No se encontró el archivo en {path}: {e}")
        raise

    except pd.errors.ParserError as e:
        logger.error(f"Error al parsear el CSV en {path}: {e}")
        raise

    except Exception as e:
        logger.error(f"Error inesperado al leer {path}: {e}")
        raise