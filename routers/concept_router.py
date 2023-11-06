from fastapi import APIRouter, HTTPException, status
from models.concept import Concepts as concept

router = APIRouter(prefix='/concept', tags=['Concepts'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/concepts')
async def concepts():
    return {'message' : {'Dentro de conceptos'}}

@router.get('/{id}')
async def my_concept(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= concept, status_code=status.HTTP_201_CREATED)
async def create_concept(concept : concept):
    return concept

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_concept_by_id(id : str):
    return id

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_concept_by_id(id : str):
    return id