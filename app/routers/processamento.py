from fastapi import APIRouter, HTTPException, Response, Query
from app.scrapping.processamento import Main as processamento_main
from typing import List, Dict, Any
from http import HTTPStatus
import json

router = APIRouter(
    prefix="/v1/processamento",
    tags=["processamento"],
    responses={404: {"description": "Item not found"}},
)

@router.get("/")
async def get_processamento() -> Dict[str, Any]:
    try:
        data = processamento_main().main()
        
        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )
            
        result = data.to_json(orient='records', indent=2, force_ascii=False)
        
        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": result
            }),
            media_type="application/json"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.get("/categoria/{categoria}")    
async def get_processamento_by_category(categoria:str = None) -> Dict[str, Any]:
    try:
        data = processamento_main.filter(categoria=categoria)

        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )

        result = data.to_json(orient='records', indent=2, force_ascii=False)

        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": result
            }),
            media_type="application/json"
        )

    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.get("/produto/{produto}")    
async def get_processamento_by_product(produto:str = None) -> Dict[str, Any]:
    try:
        data = processamento_main.filter(produto=produto)

        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )

        result = data.to_json(orient='records', indent=2, force_ascii=False)

        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": result
            }),
            media_type="application/json"
        )

    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.get("/ano/{ano}")   
async def get_processamento_by_year(ano:int = None) -> Dict[str, Any]:
    try:
        data = processamento_main.filter(ano=ano)

        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )

        result = data.to_json(orient='records', indent=2, force_ascii=False)

        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": result
            }),
            media_type="application/json"
        )

    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )
    
@router.get("/quantidade/min/{quantidade}")
async def get_processamento_by_min_quantity(quantidade:int = None) -> Dict[str, Any]:
    try:
        data = processamento_main.filter(quantidade_min=quantidade)

        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )

        result = data.to_json(orient='records', indent=2, force_ascii=False)

        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": result
            }),
            media_type="application/json"
        )

    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.get("/quantidade/max/{quantidade}")
async def get_processamento_by_max_quantity(quantidade:int = None) -> Dict[str, Any]:
    try:
        data = processamento_main.filter(quantidade_max=quantidade)

        if data.empty:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
                content=json.dumps({
                    "message": "No data found",
                    "data": []
                }),
                media_type="application/json"
            )

        result = data.to_json(orient='records', indent=2, force_ascii=False)

        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": result
            }),
            media_type="application/json"
        )

    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )

@router.get("/filter")
async def get_processamento_by_filter(
    categoria: str = Query(None, description="Filter by category"),
    produto: str = Query(None, description="Filter by product"),
    ano: int = Query(None, description="Filter by year"),
    quantidade_min: int = Query(None, description="Filter by minimum quantity"),
    quantidade_max: int = Query(None, description="Filter by maximum quantity")
):
    try:
        data = processamento_main.filter(
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
            
        result = data.to_json(orient='records', indent=2, force_ascii=False)
        
        return Response(
            status_code=HTTPStatus.OK,
            content=json.dumps({
                "message": "Data retrieved successfully",
                "data": result
            }),
            media_type="application/json"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving data: {str(e)}"
        )