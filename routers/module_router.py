from fastapi import APIRouter, HTTPException, status
from models.module import Modules as module

router = APIRouter(prefix='/module', tags=['Modules'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/moduls')
async def moduls():
    return {'message' : {'Dentro de Módulos'}}

@router.get('/{id}')
async def my_module(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= module, status_code=status.HTTP_201_CREATED)
async def create_module(module : module):
    return module

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_module_by_id(id : str):
    return id

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_module_by_id(id : str):
    return id