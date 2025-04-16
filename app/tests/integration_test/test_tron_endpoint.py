import pytest
from datetime import datetime
from app.tron.schemas import TronInfoSchema


@pytest.mark.asyncio
async def test_tron_create_and_get(ac, monkeypatch):
    fake_data = TronInfoSchema(
        address="TTestIntegration123",
        balance_trx=99.99,
        bandwidth=5000,
        energy=10000,
        date=datetime.utcnow()
    )

    async def mock_get_account_info(address: str):
        return fake_data

    monkeypatch.setattr("app.tron.router.get_account_info", mock_get_account_info)

    response_post = await ac.post("/tron/", params={"tron_address": "TTestIntegration123"})
    assert response_post.status_code == 200
    assert response_post.json()["address"] == fake_data.address

    response_get = await ac.get("/tron/")
    assert response_get.status_code == 200
    data = response_get.json()
    assert isinstance(data, list)
    assert any(item["address"] == fake_data.address for item in data)