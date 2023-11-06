from fastapi import APIRouter, HTTPException, status
from models.semester  import Semester as semester

router = APIRouter(prefix='/semester', tags=['Semesters'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/semesters')
async def semesters():
    return {'message' : {'Dentro de Semestres'}}

@router.get('/{id}')
async def my_semester(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= semester, status_code=status.HTTP_201_CREATED)
async def create_semester(semester : semester):
    return semester

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_semester_by_id(id : str):
    return id

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_semester_by_id(id : str):
    return id