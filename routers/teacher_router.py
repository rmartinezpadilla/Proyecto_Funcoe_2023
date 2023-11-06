from fastapi import APIRouter, HTTPException, status
from models.teacher import Teacher as teacher

router = APIRouter(prefix='/teacher', tags=['Teachers'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/teachers')
async def teachers():
    return {'message' : {'Dentro de Profesores'}}

@router.get('/{id}')
async def my_semester(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= teacher, status_code=status.HTTP_201_CREATED)
async def create_teacher(teacher : teacher):
    return teacher

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_teacher_by_id(id : str):
    return id

@router.put('/updatebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def update_teacher_by_identification(identification : int):
    return identification

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_teacher_by_id(id : str):
    return id

@router.delete('/deletebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_teacher_by_identification(identification : int):
    return identification