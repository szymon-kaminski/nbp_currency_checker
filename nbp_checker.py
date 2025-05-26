import requests

from dateutil import parser

URL = 'https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/?format=json'

def format_date(date_str: str) -> str:
    try:
        parsed_date = parser.parse(date_str)
        return parsed_date.strftime("%Y-%m-%d")
    except Exception:
        raise ValueError("Wrong date format.")
    




