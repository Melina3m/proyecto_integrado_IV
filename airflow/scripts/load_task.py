import sys
import os

# Añado la ruta raíz del proyecto al path para poder importar desde src
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# Importo SQLAlchemy para conectar a la base de datos
from sqlalchemy import create_engine

# Importo la función load del proyecto y el módulo de configuración
from src.load import load
from src import config

def load_data(dataframes=None):
    """
    Carga los dataframes en una base de datos SQLite.
    Usa la función load() que ya estaba implementada en el proyecto.
    
    Args:
        dataframes: Diccionario de DataFrames a cargar. 
                    Si no se pasan, se espera recibirlos desde la tarea anterior.
    """
    # Creo la conexión a la base de datos SQLite
    engine = create_engine(f"sqlite:///{config.SQLITE_BD_ABSOLUTE_PATH}", echo=False)
    
    # Si llegan los dataframes, los cargamos a la BD
    if dataframes:
        print("Iniciando carga de datos en la base de datos...")
        load(data_frames=dataframes, database=engine)
        print("Carga completada exitosamente")
        
    return True

if __name__ == "__main__":
    load_data()
