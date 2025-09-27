from fastapi import FastAPI
from .routes import deposits

app = FastAPI(title="Currency Basket Wallet (MVP)")
app.include_router(deposits.router, prefix="/api")
