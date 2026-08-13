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

    return df

def calcular_profit_margin(df):
    """
    Calcula el margen de beneficio para cada registro.

    Args:
        df (pandas.DataFrame): DataFrame con las columnas sales y profit.

    Returns:
        pandas.DataFrame: DataFrame con la columna profit_margin.
    """

    df["profit_margin"] = df["profit"] / df["sales"]

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

    return df

