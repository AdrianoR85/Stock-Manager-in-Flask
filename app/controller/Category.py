from app.model import Category

from app.extensions import logger

class CategoryController:

    @staticmethod
    def total_categories():
        result = {}
        try:
            result['data'] = Category.count_categories()
            result['status'] = 200
        except Exception as e:
            logger.exception("Error fetching total users")
            result['status'] = 500
            result['message'] = str(e)
        return result