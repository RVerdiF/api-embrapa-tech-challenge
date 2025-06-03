from fastapi import FastAPI, Query, Response
from typing import Optional, List
from http import HTTPStatus
from app.routers import (
    producao,
    comercializacao,
    processamento,
    exportacao,
    importacao,
)

app = FastAPI(
    title="API Embrapa",
    description="API para extração de informações referentes à vitivinicultura.",
    version="0.1.0",
)

app.include_router(producao.router)
app.include_router(comercializacao.router)
app.include_router(processamento.router)
app.include_router(exportacao.router)
app.include_router(importacao.router)

@app.get("/")
async def root():
    return {
        "api_name": "API Embrapa",
        "description": "API para extração de informações referentes à vitivinicultura no RS.",
        "version": "0.1.0",
        "endpoints": [
            "/v1/producao",
            "/v1/comercializacao", 
            "/v1/processamento",
            "/v1/exportacao",
            "/v1/importacao"
        ]
    }

@app.head("/")
async def head_root():
    return Response(status_code=HTTPStatus.OK)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)