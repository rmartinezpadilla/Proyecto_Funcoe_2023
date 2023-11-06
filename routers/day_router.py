from fastapi import APIRouter, HTTPException, status
from models.day import Days as day

router = APIRouter(prefix='/day', tags=['Days'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/days')
async def days():
    return {'message' : {'Dentro de días'}}

@router.get('/{id}')
async def my_day(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= day, status_code=status.HTTP_201_CREATED)
async def create_adviser(day : day):
    return day

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_day_by_id(id : str):
    return id

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_day_by_id(id : str):
    return id