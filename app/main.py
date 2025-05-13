from fastapi import FastAPI, Query
from typing import Optional, List
from app.routers import (
    producao,
    comercializacao,
    processamento
)
import sys
sys.path.append("app")

app = FastAPI(
    title="API Embrapa",
    description="API para extração de informações referentes à vitivinicultura no RS.",
    version="0.1.0",
)

app.include_router(producao.router)
app.include_router(comercializacao.router)
app.include_router(processamento.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)