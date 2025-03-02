import pandas as pd

"""
Remove field data
"""
def remove_field_data(d):
  d = d.copy()
  del d["types"]
  del d["counties"]

  return d

"""
Transform date field
"""
def transform_date_field(d):
  d = d.copy()
  d["date"] = pd.to_datetime(d["date"], format=None, errors='raise')

  return d

"""
Format response api
"""
def format_response_api(data, format_function):
  if type(data) == list:
    return list(map(format_function, data))
  else:
    raise SystemExit("Error type data")