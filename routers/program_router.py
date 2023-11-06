from fastapi import APIRouter, HTTPException, status
from models.program import Programs as program


router = APIRouter(prefix='/program', tags=['Programs'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/programs')
async def programs():
    return {'message' : {'Dentro de Programas'}}

@router.get('/{id}')
async def my_program(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= program, status_code=status.HTTP_201_CREATED)
async def create_program(program : program):
    return program

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_program_by_id(id : str):
    return id

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_program_by_id(id : str):
    return id