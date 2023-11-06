from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/user', tags=['Users'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/users')
async def users():
    return {'message' : {'Dentro de usuarios'}}