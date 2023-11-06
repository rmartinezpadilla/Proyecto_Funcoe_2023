from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/concept', tags=['Concepts'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/concepts')
async def concepts():
    return {'message' : {'Dentro de conceptos'}}