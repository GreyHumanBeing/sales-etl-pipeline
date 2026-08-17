import sqlite3
from src.logger import retornar_logger


logger = retornar_logger("load.py")

def cargar_datos(df, path):
    """
    Guarda un DataFrame en un archivo CSV.

    Args:
        df (pandas.DataFrame): DataFrame que se desea guardar.
        path (str): Ruta donde se guardará el archivo.

    Returns:
        None
    """

    try:
        df.to_csv(path, index=False)
        logger.info(f"Datos cargados correctamente en {path}")

    except Exception as e:
        logger.error(f"Error al cargar los datos en {path}: {e}")
        raise


def cargar_datos_sqlite(df, path, tabla):
    """
    Guarda un DataFrame en una base de datos SQLite.

    Args:
        df (pandas.DataFrame): DataFrame que se desea guardar.
        path (str): Ruta de la base de datos SQLite.
        tabla (str): Nombre de la tabla.

    Returns:
        None
    """

    try:
        with sqlite3.connect(path) as conexion:
            df.to_sql(
                tabla,
                conexion,
                if_exists="replace",
                index=False
            )

        logger.info(
            f"Datos cargados correctamente en SQLite: {path}, tabla: {tabla}"
        )

    except Exception as e:
        logger.error(
            f"Error al cargar los datos en SQLite: {e}"
        )
        raise