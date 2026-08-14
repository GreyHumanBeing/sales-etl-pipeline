# Sales ETL Pipeline

Proyecto de una pipeline ETL desarrollada en Python.

La pipeline toma datos desde un archivo CSV, los transforma, realiza validaciones y guarda los resultados en un nuevo CSV y en una base de datos SQLite.

## Tecnologías

- Python
- Pandas
- SQLite
- Logging

## Estructura

    sales-etl-pipeline/
    │
    ├── data/
    │   ├── raw/
    │   └── processed/
    │
    ├── database/
    │
    ├── src/
    │   ├── extract.py
    │   ├── transform.py
    │   ├── load.py
    │   ├── validate.py
    │   └── logger.py
    │
    ├── main.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## Funcionamiento

La pipeline sigue el siguiente flujo:

    CSV → Extract → Transform → Validate → Load

Los datos procesados se guardan en:

- CSV
- SQLite

Durante la ejecución se utiliza logging para registrar información y eventos importantes de la pipeline.

## Objetivo

Proyecto realizado para practicar el desarrollo de pipelines ETL con Python, procesamiento de datos, validaciones, logging y almacenamiento.

## Autor

Sebastián Arellano Scavone