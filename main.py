from src.extract import extraer_datos
from src.transform import transformar_datos
from src.load import cargar_datos
from src.validate import validar_datos
from src.logger import configurar_logger

logger = configurar_logger()

# Rutas de entrada y salida
path = "data/raw/sales.csv"
output_path = "data/processed/sales_clean.csv"


# Columnas esperadas después de las transformaciones
columnas_esperadas = [
    "ship_mode",
    "segment",
    "country",
    "city",
    "state",
    "postal_code",
    "region",
    "category",
    "sub_category",
    "sales",
    "quantity",
    "discount",
    "profit",
    "profit_margin",
]


# Tipos de datos esperados
tipos_esperados = {
    "ship_mode": "object",
    "segment": "object",
    "country": "object",
    "city": "object",
    "state": "object",
    "postal_code": "object",
    "region": "object",
    "category": "object",
    "sub_category": "object",
    "sales": "float64",
    "quantity": "int64",
    "discount": "float64",
    "profit": "float64",
    "profit_margin": "float64",
}


try:
    #1. Extraer
    logger.info("Iniciando pipeline")
    df = extraer_datos(path)
    logger.info(f"Datos extraídos correctamente: {len(df)} filas")

    # 2. Transform
    logger.info("Transformando datos")
    df_clean = transformar_datos(df)
    logger.info(f"Transformaciones aplicadas: {len(df_clean)} filas")


    # 3. Validate - Realiza todas las validaciones
    # (Existencia de nulos, columnas faltantes, tipos incorrectos)

    logger.info("Validando datos.")
    validar_datos(df_clean, columnas_esperadas, tipos_esperados)
    logger.info("Todas las validaciones fueron superadas correctamente")

    # 4. Load
    logger.info("Cargando Datos.")
    cargar_datos(df_clean, output_path)
    logger.info(f"Datos cargados correctamente en: {output_path}")

    logger.info("Pipeline finalizado correctamente")
except Exception as e:
    logger.error(f"El pipeline falló: {e}")
    raise