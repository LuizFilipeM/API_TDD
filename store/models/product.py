from store.models.base import CreateBaselModel
from store.schemas.product import ProductIn


class ProductModel(ProductIn, CreateBaselModel):
    ...
