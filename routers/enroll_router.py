from fastapi import APIRouter, HTTPException, status
from models.enroll import Enroll as enroll

router = APIRouter(prefix='/enroll', tags=['Enroll'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/enrolls')
async def enrolls():
    return {'message' : {'Dentro de Matriculas'}}

@router.get('/{id}')
async def my_enroll(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= enroll, status_code=status.HTTP_201_CREATED)
async def create_enroll(enroll : enroll):
    return enroll

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_enroll_by_id(id : str):
    return id

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_enroll_by_id(id : str):
    return id