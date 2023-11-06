from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/program', tags=['Programs'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/programs')
async def programs():
    return {'message' : {'Dentro de Programas'}}