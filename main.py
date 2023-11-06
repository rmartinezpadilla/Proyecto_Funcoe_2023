from fastapi import FastAPI
from routers import adviser_router, concept_router, day_router, enroll_router, module_router, payments_router, pensum_router, program_router, semester_router, student_router, teacher_router, user_router, document_type_router

app = FastAPI()


# Incluir routers de las entidades
app.include_router(adviser_router.router)
app.include_router(concept_router.router)
app.include_router(day_router.router)
app.include_router(enroll_router.router)
app.include_router(module_router.router)
app.include_router(payments_router.router)
app.include_router(pensum_router.router)
app.include_router(program_router.router)
app.include_router(semester_router.router)
app.include_router(student_router.router)
app.include_router(teacher_router.router)
app.include_router(user_router.router)
app.include_router(document_type_router.router)

@app.get('/')
async def root():
    return {'Mensaje' : 'Estás en la API de Funcoe Soft'}