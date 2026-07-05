from app.model import Category

class CategoryController:

    @staticmethod
    def total_categories():
        """Return the total count of categories."""
        try:
            return Category.count_categories()
        except Exception as e:
            print(f"Error occurred while fetching total categories: {e}")
            return None    