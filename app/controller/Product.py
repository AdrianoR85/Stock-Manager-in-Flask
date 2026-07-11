import logging
from app.model import Product
from typing import Optional
from app.extensions import logger

class ProductController:
    @staticmethod
    def _serialize_product(product: object) -> dict:
        return {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'quantity': product.quantity,
            'price': str(product.price),
            'image': product.image,
            'date_created': product.date_created.isoformat()
        }
    
    
    @staticmethod
    def get_all_product(limit: Optional[int]= None) -> dict:
        result = {"status": 500, "data": [], "'message": ""}
        try:
            product = Product.get_all(limit)
            result["data"] = [ProductController._serialize_product(p) for p in product]
            result["status"] = 200
        except Exception as e:
            logger.error(f"Error occurred while fetching products: {e}")
            result["status"] = 500
            result["message"] = 'An internal error occurred.'
        return result


    @staticmethod
    def get_product_by_id(product_id: int) -> dict:
        result = {"status": 500, "data": {}, "message": ""}
        try:
            product = Product.get_by_id(product_id)
            if product:
                result["data"] = ProductController._serialize_product(product)
                result["status"] = 200
            else:
                result["status"] = 404
                result["message"] = "Product not found."
        except Exception as e:
            logger.error(f"Error occurred while fetching product by ID: {e}")
            result["status"] = 500
            result["message"] = "An internal error occurred."
        return result


    @staticmethod
    def total_products() -> dict:
        result = {}
        try:
            result["data"] = Product.count_products()
            result["status"] = 200
        except Exception as e:
            logger.exception("Error fetching total products")
            result["status"] = 500
            result["message"] = str(e)
        return result
