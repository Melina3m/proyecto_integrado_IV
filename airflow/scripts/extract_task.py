import sys
import os

# Añado la ruta raíz del proyecto al path para poder importar desde src
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# Importo la función extract del proyecto y el módulo de configuración
from src.extract import extract
from src import config

def extract_data():
    """
    Extrae datos desde archivos CSV y desde una API de días festivos.
    Usa la función extract() que ya teníamos en el proyecto original.
    """
    # Ruta a la carpeta con los CSV
    csv_folder = config.DATASET_ROOT_PATH

    # URL de la API de días festivos
    public_holidays_url = config.PUBLIC_HOLIDAYS_URL

    # Mapeo de nombres de archivo CSV a nombres de tabla
    csv_table_mapping = config.get_csv_to_table_mapping()
    
    print("Iniciando extracción de datos...")
    
    # Llama a la función extract con todos los parámetros necesarios
    csv_dataframes = extract(csv_folder, csv_table_mapping, public_holidays_url)
    
    print("Extracción completada exitosamente")
    
    return csv_dataframes

# Permite ejecutar esta función manualmente si corro el script directamente
if __name__ == "__main__":
    extract_data()
