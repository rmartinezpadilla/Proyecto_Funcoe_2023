from fastapi import APIRouter, HTTPException, status
from models.document_type import Document_type as document_type

router = APIRouter(prefix='/documenttype', tags=['DocumentsType'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/documentstypes')
async def documentstypes():
    return {'message' : {'Dentro de tipos de documentos'}}

@router.get('/{id}')
async def my_document_type(id : int):
    return {'message' : f'la identificacion obtenida fué : {id}'}

@router.post('/create/', response_model= document_type, status_code=status.HTTP_201_CREATED)
async def create_document_type(document_type : document_type):
    return document_type

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_document_type_by_id(id : str):
    return id

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_document_type_by_id(id : str):
    return id