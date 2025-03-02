from typing import Dict

import requests
from pandas import DataFrame, read_csv, read_json, to_datetime
from .format import format_response_api, remove_field_data, transform_date_field

def temp() -> DataFrame:
    """Get the temperature data.
    Returns:
        DataFrame: A dataframe with the temperature data.
    """
    return read_csv("data/temperature.csv")

def get_public_holidays(public_holidays_url: str, year: str) -> DataFrame:
    """Get the public holidays for the given year for Brazil.
    Args:
        public_holidays_url (str): url to the public holidays.
        year (str): The year to get the public holidays for.
    Raises:
        SystemExit: If the request fails.
    Returns:
        DataFrame: A dataframe with the public holidays.
    """

    try:
        # TODO: Implementa esta función.
        # Debes usar la biblioteca requests para obtener los días festivos públicos del año dado.
        # La URL es public_holidays_url/{year}/BR.

        endpoint_public_holidays_br = f"{public_holidays_url}/{year}/BR"
        response = requests.get(endpoint_public_holidays_br)

        response.raise_for_status()
        data = response.json()

        # Debes eliminar las columnas "types" y "counties" del DataFrame.
        data_formated = format_response_api(data=data, format_function=remove_field_data)

        # Debes convertir la columna "date" a datetime.
        data_formated = format_response_api(data=data_formated, format_function=transform_date_field)
        return DataFrame(data_formated)
    except:
        # Debes lanzar SystemExit si la solicitud falla. Investiga el método raise_for_status
        # de la biblioteca requests.
        raise SystemExit("Error process request")


def extract(
    csv_folder: str, csv_table_mapping: Dict[str, str], public_holidays_url: str
) -> Dict[str, DataFrame]:
    """Extract the data from the csv files and load them into the dataframes.
    Args:
        csv_folder (str): The path to the csv's folder.
        csv_table_mapping (Dict[str, str]): The mapping of the csv file names to the
        table names.
        public_holidays_url (str): The url to the public holidays.
    Returns:
        Dict[str, DataFrame]: A dictionary with keys as the table names and values as
        the dataframes.
    """
    dataframes = {
        table_name: read_csv(f"{csv_folder}/{csv_file}")
        for csv_file, table_name in csv_table_mapping.items()
    }

    holidays = get_public_holidays(public_holidays_url, "2017")

    dataframes["public_holidays"] = holidays

    return dataframes
