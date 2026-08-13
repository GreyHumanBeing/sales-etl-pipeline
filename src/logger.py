import logging

import logging


def configurar_logger():
    """
    Configura el sistema de logging del proyecto.

    Returns:
        logging.Logger: Logger configurado.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(__name__)