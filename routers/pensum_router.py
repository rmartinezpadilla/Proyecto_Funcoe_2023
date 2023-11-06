from fastapi import APIRouter, HTTPException, status
from models.pensum import Pensum as pensum

router = APIRouter(prefix='/pensum', tags=['Pensums'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/pensums')
async def pensums():
    return {'message' : {'Dentro de Pensum'}}

@router.get('/{id}')
async def my_pensum(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= pensum, status_code=status.HTTP_201_CREATED)
async def create_pensum(pensum : pensum):
    return pensum

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_pensum_by_id(id : str):
    return id

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_pensum_by_id(id : str):
    return id