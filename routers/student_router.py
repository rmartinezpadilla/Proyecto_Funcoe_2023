from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/student', tags=['Students'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/students')
async def students():
    return {'message' : {'Dentro de Estudiantes'}}