import sys
import os

# Añado la ruta raíz del proyecto al path para poder importar desde src
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# Importo SQLAlchemy para conectarme a la base de datos
from sqlalchemy import create_engine

# Importo la función que ejecuta las transformaciones y la config
from src.transform import run_queries
from src import config

def transform_data():
    """
    Ejecuta las transformaciones necesarias en la base de datos.
    Usa la función run_queries() que ya está hecha en el proyecto.
    """
    # Creo la conexión a la base de datos SQLite
    engine = create_engine(f"sqlite:///{config.SQLITE_BD_ABSOLUTE_PATH}", echo=False)
    
    # Ejecuto las consultas de transformación
    print("Iniciando transformaciones de datos...")
    query_results = run_queries(database=engine)
    print("Transformaciones completadas exitosamente")
    
    return True

if __name__ == "__main__":
    transform_data()
