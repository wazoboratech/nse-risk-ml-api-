from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def calculate_risk(stock):
    score = 50
    if stock["pe_ratio"]>20: score += 15
    if stock["pe_ratio"]<10: score -= 10
    if stock["market_cap"]<5000000: score += 10
    return max(1, min(100, score))

@app.get("/")
def home():
    return {"message": "NSE Risk API v2 is running"}

@app.get("/stocks")
def get_stocks():
    with open("nse_data.json", "r") as f:
        data = json.load(f)
        return {"stocks": data}
    for stock in data:
        stock["risk_score"] = calculate_risk(stock)

    return{"stocks": data} 

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)