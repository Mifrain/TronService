from datetime import datetime

from fastapi import HTTPException

from tronpy import Tron
from tronpy.providers import HTTPProvider

from app.config import settings
from app.tron.schemas import TronInfoSchema


client = Tron(HTTPProvider(api_key=settings.TRON_API_KEY))

# для теста использовал этот адрес TPwezUWpEGmFBENNWJHwXHRG1D2NCEEt5s
async def get_account_info(address: str) -> TronInfoSchema:
    try:
        account = client.get_account(address)
        resources = client.get_account_resource(address)

        return TronInfoSchema(
            address=address,
            balance_trx=account.get('balance', 0) / 1_000_000,
            bandwidth=resources.get("free_net_usage", 0),
            energy=resources.get("energy_usage", 0),
            date=datetime.utcnow()
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail="Неверный TRON адрес")

    