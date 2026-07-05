from app.model import Product


class ProductController:
    @staticmethod
    def get_all_products():
        return Product.get_all()

    @staticmethod
    def total_products():
        try:
            return Product.count_products()
        except Exception as e:
            print(f"Error occurred while fetching total products: {e}")
            return None
