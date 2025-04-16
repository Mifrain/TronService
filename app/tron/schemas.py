from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TronInfoSchema(BaseModel):
    address: str
    balance_trx: float
    bandwidth: int
    energy: int
    date: datetime

    model_config = ConfigDict(from_attributes=True)