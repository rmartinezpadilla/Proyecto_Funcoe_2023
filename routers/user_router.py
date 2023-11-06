from fastapi import APIRouter, HTTPException, status
from models.user import User as user


router = APIRouter(prefix='/user', tags=['Users'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/users')
async def users():
    return {'message' : {'Dentro de usuarios'}}

@router.get('/{id}')
async def my_semester(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= user, status_code=status.HTTP_201_CREATED)
async def create_user(user : user):
    return user

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_user_by_id(id : str):
    return id

@router.put('/updatebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def update_user_by_identification(identification : int):
    return identification

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_by_id(id : str):
    return id

@router.delete('/deletebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_by_identification(identification : int):
    return identification