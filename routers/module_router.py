from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/module', tags=['Modules'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/moduls')
async def moduls():
    return {'message' : {'Dentro de Módulos'}}