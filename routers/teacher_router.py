from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/teacher', tags=['Teachers'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/teachers')
async def teachers():
    return {'message' : {'Dentro de Profesores'}}