from fastapi import FastAPI
from fastapi.params import Depends
from typing import List
#from db.models.adviser import Adviserdb as adv
from db.models import adviser
from starlette.responses import RedirectResponse
from db.connection_to_MySQL import SessionLocal, engine, Base
from sqlalchemy.orm import Session

adviser.Base.metadata.create_all(bind = engine)



app = FastAPI()

def get_db():
    try:
        db =  SessionLocal()
        yield db                
    except:
        db.close()

# @app.get('/')
# async def main():
#     return RedirectResponse(url='/docs/')

@app.get('/advisers/')
async def show_advisers(db : Session=Depends(get_db)):
    advisers =  db.query(adviser.Adviserdb).all()
    return advisers