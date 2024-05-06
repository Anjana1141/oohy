#data_utils.py
import datetime

def convert_to_sql_date(dt):
    # Format the datetime object into a string
    date_str = dt.strftime('%Y-%m-%d')  # Format: YYYY-MM-DD

    # Construct the SQL representation
    sql_date_representation = f"TO_DATE('{date_str}', 'YYYY-MM-DD')"

    return sql_date_representation

# Example usage
# dt = datetime.datetime(2022, 4, 25)
# sql_date = convert_to_sql_date(dt)
# print(sql_date)
