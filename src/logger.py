import logging


def configurar_logger():
    """
    Configura el sistema de logging del proyecto.

    Returns:
        None
    """
    handlers = [
        logging.StreamHandler(),  # este manda a la consola
        logging.FileHandler("pipeline.log")  # este manda a un archivo
    ]

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=handlers
    )




def retornar_logger(script_name):
    """
    Retorna un objeto logger para ser utilizado en el logueo de eventos

    Args:
        script_name (str): Nombre de la script que esta llamando a la funcion.

    Returns:
        logging.Logger: Objeto logger.
    """
    return logging.getLogger(script_name)