from typing import List

from fastapi import APIRouter

from app.tron.schemas import TronInfoSchema
from app.tron.services import TronService
from app.tron.tron_client import get_account_info

router = APIRouter(prefix="/tron", tags=["Tron"])

@router.get("/")
async def get_tron() -> List[TronInfoSchema]:
    all_trons = await TronService.find_all()
    return all_trons

@router.post("/")
async def create_tron(tron_address: str):
    info: TronInfoSchema = await get_account_info(tron_address)
    await TronService.add(**info.model_dump())
    return info