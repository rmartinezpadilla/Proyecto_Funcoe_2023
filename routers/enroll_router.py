from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/enroll', tags=['Enroll'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/enrolls')
async def enrolls():
    return {'message' : {'Dentro de Matriculas'}}