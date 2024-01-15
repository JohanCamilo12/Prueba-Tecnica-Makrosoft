from app.settings.database import database


class WorkersService:
    def __init__(self):
        self.repository = database

    async def find_workers(self, workers_id: int):
        """Get register in the persistence"""

        result = await self.repository.workers.find_first(where={"id": workers_id})

        return result

    async def find_all_workers(self):
        """Get all registers in the persistence"""

        result = await self.repository.workers.find_many(include={"soportes": True})

        return result

    async def create_workers(self, workers):
        """Save register in the persistence"""

        result = await self.repository.workers.create(data={"nombre":workers.nombre, "complejidad_acumulada":workers.complejidad_acumulada})

        return result
    
    async def create_support(self, id, support):
        """Save register in the persistence"""

        #workers = await self.repository.workers.find_first(where={"id": id})
        #result = await self.repository.workers.update
        
        if(support.complejidad in [10,20,30]): 
               
            worker = await self.repository.workers.find_first(where={"id": id})
               
            result = await self.repository.workers.update(
                where= {
                    "id": id,
                },
                data= {
                    "complejidad_acumulada": support.complejidad + worker.complejidad_acumulada,
                    "soportes": {
                    "create": [{
                        "descripcion":support.descripcion, "complejidad":support.complejidad
                    }],
                    },
                },
                include= {
                    "soportes": True,
                },
                
                
            )
            return result
        return {'error': 'la complejidad no esta en 10, 20 y 30'}
        
        #result = await self.repository.support.update(
        
        # const updateAuthor = await prisma.user.update({
        #     where: {
        #         id: 20,
        #     },
        #     data: {
        #         posts: {
        #         connect: {
        #             id: 4,
        #         },
        #         },
        #     },
        #     })
        
        

    async def update_workers(self, workers_id: int, workers):
        """Update register in the persistence"""

        result = await self.repository.workers.update(
            where={"id": workers_id},
            data=vars(workers),
        )

        return result

    async def delete_workers(self, workers_id: int):
        """Delete register in the persistence"""

        result = await self.repository.workers.delete(where={"id": workers_id})

        return result
