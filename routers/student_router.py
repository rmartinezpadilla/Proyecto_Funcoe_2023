from fastapi import APIRouter, HTTPException, status
from models.student import Student as student

router = APIRouter(prefix='/student', tags=['Students'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/students')
async def students():
    return {'message' : {'Dentro de Estudiantes'}}

@router.get('/{id}')
async def my_semester(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= student, status_code=status.HTTP_201_CREATED)
async def create_semester(student : student):
    return student

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_student_by_id(id : str):
    return id

@router.put('/updatebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def update_student_by_identification(identification : int):
    return identification

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_student_by_id(id : str):
    return id

@router.delete('/deletebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_student_by_identification(identification : int):
    return identification