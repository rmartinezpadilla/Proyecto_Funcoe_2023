from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/pensum', tags=['Pensums'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/pensums')
async def pensums():
    return {'message' : {'Dentro de Pensum'}}