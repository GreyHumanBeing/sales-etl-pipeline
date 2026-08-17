from src.extract import extraer_datos
from src.transform import transformar_datos
from src.load import cargar_datos, cargar_datos_sqlite
from src.validate import validar_datos
from src.logger import configurar_logger, retornar_logger

configurar_logger()
logger = retornar_logger("main.py")

# Rutas de entrada y salida
database_path = "database/sales.db"
tabla = "sales"
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
    logger.info("Iniciando Pipeline...")
    #1. Extract
    df = extraer_datos(path)

    #2. Transform
    df_clean = transformar_datos(df)

    #3. Validate
    validar_datos(df_clean, columnas_esperadas, tipos_esperados)

    #4. Load
    cargar_datos(df_clean, output_path)
    cargar_datos_sqlite(df_clean, database_path, tabla)

    logger.info("Pipeline finalizado correctamente")

except Exception as e:
    logger.error(f"El pipeline falló: {e}")
    raise