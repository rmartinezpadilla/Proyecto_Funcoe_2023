from fastapi import APIRouter, HTTPException, status
from db.db_client_MySQL import conn
from db.models.adviser import Adviserdb as adv
from uuid import uuid4 as uuid
from db.schemas.adviser_schema import adviser_schema

router = APIRouter(prefix='/adviser', tags=['Adviser'], responses={404 : {'message' : 'No encontrado'}})

@router.get('/advisers')
async def advisers():
    return {'message' : {'Dentro de adviser'}}

@router.get('/{identification}')
async def adviser(indentificacion : int):
    return {'message' : f'la identificacion obtenida fué : {indentificacion}'}

@router.post('/create/', response_model = adv, status_code=status.HTTP_201_CREATED)
async def create_adviser(adv : adv):
    
    if type(search_adviser(adv.identification_card)) == tuple:
    #if len(search_adviser(adv.identification_card)) > 0 | :
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'El asesor con número de cédula {adv.identification_card} ya existe'
         )
                      
    adv.id = str(uuid())
    cursor = conn.cursor()
    query = "INSERT INTO asesores (uuid, id_document_type, identification_card, first_name, last_name, phone, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(query, (adv.id, adv.document_type, adv.identification_card, adv.first_name, adv.last_name, adv.phone, adv.created_at))
        conn.commit()
        id = cursor.lastrowid
        cursor.close()
        return adv
    
    except:
        HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f'el tipo de documento no existe {id}'
            )

@router.put('/updatebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_adviser_by_id(id : str):
    return id

@router.put('/updatebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def update_adviser_by_identification(identification : int):
    return identification

@router.delete('/deletebyidentification/{identification}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_adviser_by_identification(identification : int):
    return identification

@router.delete('/deletebyid/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_adviser_by_id(id : str):
    return id

# -------------- METODOS -------------------
def search_adviser(identification : int):          
    
    cursor = conn.cursor()
    query = "SELECT * FROM asesores WHERE identification_card=%s"
    cursor.execute(query, (identification,))
    my_adviser = cursor.fetchone() 
    #print(my_adviser)  
    return my_adviser
    
    
