from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/semester', tags=['Semesters'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/semesters')
async def semesters():
    return {'message' : {'Dentro de Semestres'}}