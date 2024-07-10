from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, BaseModel, Field

from store.schemas.base import BaseSchemaMixin, OutMixin


class ProductBase(BaseModel):
    name: str = Field(..., UNIQUE=True, description="Product name")
    quantity: int = Field(..., description="Quantity name")
    price: Decimal = Field(..., description="Price name")
    status: bool = Field(..., description="Status name")
    # os '...' indicam obrigatoriedade de campo


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutMixin):
    ...


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(ProductIn):
    quantity: Optional[int] = Field(None, description="Quantity name")
    status: Optional[bool] = Field(None, description="Status name")
    price: Optional[Decimal_] = Field(None, description="Price name")


class ProductUpdateOut(ProductUpdate, OutMixin):
    ...
