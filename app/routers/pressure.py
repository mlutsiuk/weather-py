from fastapi import APIRouter, HTTPException

from app.schemas.humidity import ProductModel, ProductCreate, ProductUpdate
from app.utils import pressure as product_utils

router = APIRouter()


@router.get("/products")
async def products_index():
    return await product_utils.get_products()
    # return {"message": "products:index"}


@router.post("/products", response_model=ProductModel, status_code=201)
async def products_store(product: ProductCreate):
    product_id = await product_utils.create_product(product)

    return await product_utils.find_product(product_id)


@router.get("/products/{product_id}", response_model=ProductModel)
async def products_show(product_id: int):
    product = await product_utils.find_product(product_id)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.put("/products/{product_id}", response_model=ProductModel)
async def products_update(product_id: int, product_data: ProductUpdate):
    product = await product_utils.find_product(product_id)
    if product:
        await product_utils.update_product(product_id, product_data)
        return await product_utils.find_product(product_id)
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/products/{product_id}")
async def products_destroy(product_id: int):
    await product_utils.destroy(product_id)
