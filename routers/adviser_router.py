from fastapi import APIRouter, HTTPException, status
#from models.adviser import Adviser

router = APIRouter(prefix='/adviser', tags=['Adviser'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/advisers')
async def advisers():
    return {'message' : {'Dentro de adviser'}}