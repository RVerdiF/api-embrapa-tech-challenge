from fastapi import APIRouter, HTTPException, Response, Query
from app.scrapping.comercializacao import Main as comercializacao_main
from typing import List, Dict, Any
from http import HTTPStatus
import json

router = APIRouter(
    prefix="/v1/comercializacao",
    tags=["comercializacao"],
    responses={404: {"description": "Item not found"}},
)

@router.get("/")
async def get_comercializacao() -> Dict[str, Any]:
    try:
        data = comercializacao_main.main()
        
        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )
            
        result = data.to_json(orient='records', force_ascii=False)
        
        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": json.loads(result)
            }),
            media_type="application/json"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.head("/")
async def head_comercializacao():
    try:
        data = comercializacao_main.main()
        status_code = HTTPStatus.OK if not data.empty else HTTPStatus.NO_CONTENT
        return Response(status_code=status_code)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.get("/categoria/{categoria}")
async def get_comercializacao_by_category(categoria:str = None):
    try:
        data = comercializacao_main.filter(categoria=categoria)
        
        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )
            
        result = data.to_json(orient='records', force_ascii=False)
        
        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": json.loads(result)
            }),
            media_type="application/json"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.head("/categoria/{categoria}")
async def head_comercializacao_by_category(categoria:str = None):
    try:
        data = comercializacao_main.filter(categoria=categoria)
        status_code = HTTPStatus.OK if not data.empty else HTTPStatus.NO_CONTENT
        return Response(status_code=status_code)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.get("/produto/{produto}")
async def get_comercializacao_by_product(produto:str = None):
    try:
        data = comercializacao_main.filter(produto=produto)
        
        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )
            
        result = data.to_json(orient='records', force_ascii=False)
        
        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": json.loads(result)
            }),
            media_type="application/json"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.head("/produto/{produto}")
async def head_comercializacao_by_product(produto:str = None):
    try:
        data = comercializacao_main.filter(produto=produto)
        status_code = HTTPStatus.OK if not data.empty else HTTPStatus.NO_CONTENT
        return Response(status_code=status_code)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.get("/ano/{ano}")
async def get_comercializacao_by_year(ano:int = None):
    try:
        data = comercializacao_main.filter(ano=ano)
        
        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )
            
        result = data.to_json(orient='records', force_ascii=False)
        
        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": json.loads(result)
            }),
            media_type="application/json"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.head("/ano/{ano}")
async def head_comercializacao_by_year(ano:int = None):
    try:
        data = comercializacao_main.filter(ano=ano)
        status_code = HTTPStatus.OK if not data.empty else HTTPStatus.NO_CONTENT
        return Response(status_code=status_code)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )
    
@router.get("/quantidade/min/{quantidade}")
async def get_comercializacao_by_min_quantity(quantidade:int = None):
    try:
        data = comercializacao_main.filter(quantidade_min=quantidade)
        
        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )
            
        result = data.to_json(orient='records', force_ascii=False)
        
        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": json.loads(result)
            }),
            media_type="application/json"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.head("/quantidade/min/{quantidade}")
async def head_comercializacao_by_min_quantity(quantidade:int = None):
    try:
        data = comercializacao_main.filter(quantidade_min=quantidade)
        status_code = HTTPStatus.OK if not data.empty else HTTPStatus.NO_CONTENT
        return Response(status_code=status_code)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.get("/quantidade/max/{quantidade}")
async def get_comercializacao_by_max_quantity(quantidade:int = None):
    try:
        data = comercializacao_main.filter(quantidade_max=quantidade)
        
        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )
            
        result = data.to_json(orient='records', force_ascii=False)
        
        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": json.loads(result)
            }),
            media_type="application/json"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.head("/quantidade/max/{quantidade}")
async def head_comercializacao_by_max_quantity(quantidade:int = None):
    try:
        data = comercializacao_main.filter(quantidade_max=quantidade)
        status_code = HTTPStatus.OK if not data.empty else HTTPStatus.NO_CONTENT
        return Response(status_code=status_code)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )
    
@router.get("/filter")
async def get_comercializacao_by_filter(
    categoria: str = Query(None, description="Filter by category"),
    produto: str = Query(None, description="Filter by product"),
    ano: int = Query(None, description="Filter by year"),
    quantidade_min: int = Query(None, description="Filter by minimum quantity"),
    quantidade_max: int = Query(None, description="Filter by maximum quantity")
):
    try:
        data = comercializacao_main.filter(
            categoria=categoria,
            produto=produto, 
            ano=ano,
            quantidade_min=quantidade_min,
            quantidade_max=quantidade_max
        )
        
        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found", 
                    "data": []
                }),
                media_type="application/json"
            )
            
        result = data.to_json(orient='records', force_ascii=False)
        
        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": json.loads(result)
            }),
            media_type="application/json"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.head("/filter")
async def head_comercializacao_by_filter(
    categoria: str = Query(None, description="Filter by category"),
    produto: str = Query(None, description="Filter by product"),
    ano: int = Query(None, description="Filter by year"),
    quantidade_min: int = Query(None, description="Filter by minimum quantity"),
    quantidade_max: int = Query(None, description="Filter by maximum quantity")
):
    try:
        data = comercializacao_main.filter(
            categoria=categoria,
            produto=produto, 
            ano=ano,
            quantidade_min=quantidade_min,
            quantidade_max=quantidade_max
        )
        status_code = HTTPStatus.OK if not data.empty else HTTPStatus.NO_CONTENT
        return Response(status_code=status_code)
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )