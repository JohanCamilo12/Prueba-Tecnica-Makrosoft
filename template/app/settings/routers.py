from app.workers.router import router as workers_router

#Mapea los endpoints tener la aplicacion modularizada, punto de anclanje
#Alta cohecion, bajo aclopamiento
#sf mas flexible, mayor acceso rapido a la base de datos
#prisma es un ORM que permite 
routers = [
    workers_router
]

