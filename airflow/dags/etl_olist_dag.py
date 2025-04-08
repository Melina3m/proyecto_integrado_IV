from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Agrego rutas para poder importar scripts que están fuera del directorio actual
dag_path = os.path.dirname(os.path.abspath(__file__))
airflow_path = os.path.dirname(dag_path)
project_path = os.path.dirname(airflow_path)
sys.path.append(project_path)
sys.path.append(airflow_path)

# Importo las funciones que hacen cada parte del proceso ETL
from scripts.extract_task import extract_data
from scripts.load_task import load_data
from scripts.transform_task import transform_data

# Defino argumentos por defecto para todas las tareas del DAG
default_args = {
    'owner': 'airflow',                  # Usuario responsable
    'depends_on_past': False,            # No depende de ejecuciones pasadas
    'email_on_failure': False,           # No envía correos si falla
    'email_on_retry': False,             # Tampoco si reintenta
    'retries': 1,                        # Solo reintenta una vez si falla
    'retry_delay': timedelta(minutes=5), # Espera 5 min antes de reintentar
}

# Creo el DAG principal del pipeline ETL
with DAG(
    'etl_olist_pipeline',                  # ID del DAG
    default_args=default_args,             # Aplico argumentos por defecto
    description='Pipeline ELT para datos de Olist E-commerce',
    schedule_interval='@daily',            # Se ejecuta todos los días
    start_date=datetime(2023, 1, 1),       # Fecha de inicio
    catchup=False,                         
    tags=['olist', 'ecommerce', 'etl'],    # Etiquetas para organizar en Airflow
) as dag:

    # Tarea 1: Extrae los datos desde las fuentes
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    # Tarea 2: Carga los datos a SQLite
    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
        op_kwargs={'dataframes': None},
        provide_context=True,
    )

    # Tarea 3: Aplica transformaciones a los datos
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    # Defino el orden: primero extraer, luego cargar, luego transformar
    extract_task >> load_task >> transform_task
