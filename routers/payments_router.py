from fastapi import APIRouter, HTTPException, status
from models.payment import Payments as payment

router = APIRouter(prefix='/payments', tags=['Payments'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/payments')
async def payments():
    return {'message' : {'Dentro de pagos'}}

@router.get('/{id}')
async def my_payment(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= payment, status_code=status.HTTP_201_CREATED)
async def create_payment(payment : payment):
    return payment

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_payment_by_id(id : str):
    return id

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment_by_id(id : str):
    return id