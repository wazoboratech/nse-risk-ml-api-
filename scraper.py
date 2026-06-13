import json

def scape_nse():
    stocks = [
        {"ticker": "SCOM", "name": "Safareicom PLC", "price": 13.45, "pe_ratio": 12.1, "market_cap": 53800000000},
        {"ticker": "EQTY", "name": "equity group", "price":  44.50, "pe_ratio": 3.5, "market_cap": 13800000000},
        {"ticker": "KCB", "name": "KCB group", "price": 38.90, "pe_ratio": 3.0, "market_cap": 12200000000},
        {"ticker": "EABL", "name": "East African breweries", "price": 165.00, "pe_ratio": 5.6, "market_cap": 65400000000}]

    with open("nse_data.json", "w") as f:
        json.dump(stocks, f, indent=2)

    print(f"success: Saved {len(stocks)} stocks to nse_data.json")

if __name__=="__main__":
    scape_nse()