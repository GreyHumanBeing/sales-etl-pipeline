def existencia_nulos(df):
    """
    Verifica que el DataFrame no contenga valores nulos.

    Args:
        df (pandas.DataFrame): DataFrame a validar.

    Returns:
        bool: True si no existen valores nulos, False en caso contrario.
    """

    return not df.isnull().values.any()

def checkear_duplicados(df):
    """
        Verifica que el DataFrame no contenga valores duplicados.

        Args:
            df (pandas.DataFrame): DataFrame a validar.

        Returns:
            bool: True si no existen valores duplicados, False en caso contrario.
    """

    return not df.duplicated().any()

def validar_columnas(df, columnas_esperadas):
    """
    Verifica que el DataFrame contenga todas las columnas esperadas.

    Args:
        df (pandas.DataFrame): DataFrame a validar.
        columnas_esperadas (list): Lista de columnas requeridas.

    Returns:
        list: List de columnas faltantes(si las hay).
    """

    columnas_faltantes = []

    for col in columnas_esperadas:
        if col not in df.columns:
            columnas_faltantes.append(col)

    return columnas_faltantes

def validar_tipo_de_datos(df, tipos_esperados):
    """
    Verifica que las columnas tengan los tipos de datos esperados.

    Args:
        df (pandas.DataFrame): DataFrame a validar.
        tipos_esperados (dict): Tipos esperados por columna.

    Returns:
        dict: Diccionario con las columnas que tienen tipos incorrectos.
    """

    tipos_invalidos = {}

    for col, tipo_esperado in tipos_esperados.items():
        if df[col].dtype != tipo_esperado:
            tipos_invalidos[col] = {
                "esperado": tipo_esperado,
                "actual": df[col].dtype
            }

    return tipos_invalidos

def validar_datos(df, columnas_esperadas, tipos_esperados):
    """
    Ejecuta todas las validaciones del DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame a validar.
        columnas_esperadas (list): Columnas requeridas.
        tipos_esperados (dict): Tipos de datos requeridos.

    Raises:
        ValueError: Si alguna validación falla.
    """

    if not existencia_nulos(df):
        raise ValueError("El DataFrame contiene valores nulos.")

    columnas_faltantes = validar_columnas(
        df,
        columnas_esperadas
    )

    if columnas_faltantes:
        raise ValueError(
            f"Faltan las siguientes columnas: {columnas_faltantes}"
        )

    tipos_incorrectos = validar_tipo_de_datos(
        df,
        tipos_esperados
    )

    if tipos_incorrectos:
        raise ValueError(
            f"Tipos de datos incorrectos: {tipos_incorrectos}"
        )
