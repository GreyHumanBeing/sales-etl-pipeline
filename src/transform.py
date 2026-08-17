from src.logger import retornar_logger

logger = retornar_logger("transform.py")

def normalizar_columnas(df):
    """
        Convierte los nombres de las columnas a snake_case.

        Args:
            df (pandas.DataFrame): DataFrame cuyas columnas serán normalizadas.

        Returns:
            pandas.DataFrame: DataFrame con los nombres de columnas normalizados.
    """
    columnas = []

    for col in df.columns:
        nuevo_nombre = "_".join(col.lower().split()).replace("-", "_")
        columnas.append(nuevo_nombre)

    df.columns = columnas
    logger.info("Columnas normalizadas.")
    return df


def convertir_tipos(df):
    """
    Convierte columnas al tipo de dato adecuado según su significado.

    Args:
        df (pandas.DataFrame): DataFrame a transformar.

    Returns:
        pandas.DataFrame: DataFrame con tipos ajustados.
    """

    df["postal_code"] = df["postal_code"].astype(str)
    logger.info("Tipos de datos convertidos.")
    return df

def calcular_profit_margin(df):
    """
    Calcula el margen de beneficio para cada registro.

    Args:
        df (pandas.DataFrame): DataFrame con las columnas sales y profit.

    Returns:
        pandas.DataFrame: DataFrame con la columna profit_margin.

    Raises:
        ValueError: Si al menos una fila contiene sales = 0(Valor incorrecto)


    """
    if (df['sales']==0).any():
        logger.error("La columna sales contiene al menos un valor = 0. Deteniendo Pipeline.. ")
        raise ValueError("Error de valor en columna sales.")

    df["profit_margin"] = df["profit"] / df["sales"]
    logger.info("Columna profit_margin creada.")
    return df

def transformar_datos(df):
    """
    Aplica todas las transformaciones al DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame extraído.

    Returns:
        pandas.DataFrame: DataFrame transformado.
    """

    df = normalizar_columnas(df)
    df = convertir_tipos(df)
    df = calcular_profit_margin(df)
    logger.info("Todas las transformaciones fueron realizadas correctamente.")
    return df

