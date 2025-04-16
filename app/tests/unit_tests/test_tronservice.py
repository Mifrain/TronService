import pytest
from datetime import datetime
from app.tron.schemas import TronInfoSchema
from app.tron.services import TronService


async def test_tronservice_add_and_find():
    test_data = TronInfoSchema(
        address="TTestUnit123",
        balance_trx=12.34,
        bandwidth=100,
        energy=200,
        date=datetime.utcnow()
    )

    await TronService.add(**test_data.model_dump())
    result = await TronService.find_all(address="TTestUnit123")

    assert len(result) == 1
    record = result[0]
    assert record.address == test_data.address
    assert record.balance_trx == test_data.balance_trx
