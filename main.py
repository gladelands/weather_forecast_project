from create_db import create_DB_connection, close_connection
from create_pandas_df_from_json import convert_dict_to_df
from update_db import update_db
from transform import keep_columns, change_col_name, convert_kelvin_to_celsius, set_datetime_col_as_row_index
from get_weather_data_from_OpenWeatherMap import get_current_weather_data_from_OpenWeatherMap, write_weather_data_in_json_file
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--city_id", default="293397", help="enter city id")
args = parser.parse_args()
if args.city_id:
    print("city id inserted")

returned_connection = create_DB_connection()
filename = write_weather_data_in_json_file(
    get_current_weather_data_from_OpenWeatherMap(args.city_id))
new_df_to_sql = set_datetime_col_as_row_index(convert_kelvin_to_celsius(
    change_col_name(keep_columns(convert_dict_to_df(filename)))))

update_db(new_df_to_sql, returned_connection)

close_connection(returned_connection)
