from fastapi import APIRouter, HTTPException, status
from models.adviser import Adviser as adviser

router = APIRouter(prefix='/adviser', tags=['Adviser'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/advisers')
async def advisers():
    return {'message' : {'Dentro de adviser'}}


@router.get('/{identification}')
async def adviser(indentificacion : int):
    return {'message' : f'la identificacion obtenida fué : {indentificacion}'}

@router.post('/create/', response_model= adviser, status_code=status.HTTP_201_CREATED)
async def create_adviser(adviser : adviser):
    return adviser

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_adviser_by_id(id : str):
    return id

@router.put('/updatebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def update_adviser_by_identification(identification : int):
    return identification

@router.delete('/deletebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_adviser_by_identification(identification : int):
    return identification

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_adviser_by_id(id : str):
    return id