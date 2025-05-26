from nbp_checker import format_date, fetch_exchange_rate

import sys


def get_currency() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return input("Enter the currency code (e.g. USD, EUR): ").strip()


def get_date() -> str:
    try:
        return sys.argv[2]
    except IndexError:
        return input("Enter the date (e.g. 2025-05-26): ").strip()
    

currency = get_currency()
user_input_date = get_date()
