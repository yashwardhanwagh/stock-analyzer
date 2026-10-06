import requests
import json
import os

from datetime import date
from dotenv import load_dotenv

load_dotenv()

os.makedirs("cache", exist_ok=True)

def get_stock_data(symbol):
    cache_file = f"cache/{symbol}.json"

    # Check local cache
    if os.path.exists(cache_file):

        with open(cache_file,"r") as file:
            cache_data =  json.load(file)

        cache_date =  cache_data["latest_price"]["trade_date"]
        today = str(date.today())

        if cache_date == today:
            return cache_data

        else:
            print("Cached data is outdated. Fetching fresh data...")

    # API REQUEST
    api_key = os.getenv("BHARATSTOCK_API_KEY")
    url =  f"https://bharatstockapi.com/v1/stocks/{symbol}"

    headers = {
    "X-API-key": api_key
}
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 404:
        raise ValueError(f"Stock {symbol} was not found.")

    if response.status_code == 401:
        raise ValueError("Invalid API Key.")

    if response.status_code == 429:
        raise ValueError("API request limit reached.")

    response.raise_for_status()

    data = response.json()

    # Save API response
    with open(cache_file, "w") as file:
        json.dump(data, file, indent=4)

    
    return data


   

def process_stock_data(data):
    stock = {
        "name": data["company_name"],
        "symbol": data["symbol"],
        "sector": data["sector"],
        "industry": data["industry"],
        "price": data["latest_price"]["close"],
        "eps": data["metrics"]["eps"],
        "book_value_per_share": data["metrics"]["book_value_per_share"],
        "shares_outstanding": data["metrics"]["shares_outstanding"],
        "roe" : data["metrics"]["roe"],
        "roce" : data["metrics"]["roce"],
        "debt_to_equity": data["metrics"]["debt_to_equity"],
        "net_margin": data["metrics"]["net_margin"],
        "eps_growth_yoy": data["metrics"]["eps_growth_yoy"],
        "revenue_growth_yoy": data["metrics"]["revenue_growth_yoy"],
        "cash_flow_operating": data["metrics"]["cash_flow_operating"],
        "free_cash_flow": data["metrics"]["free_cash_flow"],
        "cfo_to_net_profit": data["metrics"]["cfo_to_net_profit"],
        "profit_growth_yoy" : data["metrics"]["profit_growth_yoy"],
        "pe_ratio" : data["metrics"]["pe_ratio"],
        "pb_ratio" : data["metrics"]["pb_ratio"],
        "peg_ratio" : data["metrics"]["peg_ratio"],
        "ev_to_ebitda" : data["metrics"]["ev_to_ebitda"],
        "earnings_yield": data["metrics"]["earnings_yield"]
    }
    return stock


