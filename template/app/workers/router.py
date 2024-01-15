from fastapi import APIRouter
from app.workers.schema import SupportBase, WorkerBase

from app.workers.services import WorkersService

router = APIRouter(
    prefix="/workers",
    tags=["Workers"],
)

workers_service = WorkersService()


@router.get("")
async def get_all_workers():
    return await workers_service.find_all_workers()


@router.get("/{id}")
async def get_workers(id: int):
    return await workers_service.find_workers(id)


@router.post("")
async def create_workers(workers:WorkerBase):
    return await workers_service.create_workers(workers)

@router.post("/{id}")
async def create_support(id: int, support:SupportBase):
    return await workers_service.create_support(id, support)


@router.put("/{id}")
async def update_workers(id: int, workers):
    return await workers_service.update_workers(id, workers)


@router.delete("/{id}")
async def delete_workers(id: int):
    return await workers_service.delete_workers(id)
