from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix='/payments', tags=['Payments'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/payments')
async def payments():
    return {'message' : {'Dentro de pagos'}}