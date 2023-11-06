from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/day', tags=['Days'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/days')
async def days():
    return {'message' : {'Dentro de días'}}