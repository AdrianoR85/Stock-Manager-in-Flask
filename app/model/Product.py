from app.extensions import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=True)
    quantity = db.Column(db.Integer, nullable=True, default=0)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image = db.Column(db.Text(), nullable=True)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_updated = db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    status = db.Column(db.Boolean, default=1, nullable=True)

    user_created = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    category = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)

    usuario = db.relationship("User")
    categoria = db.relationship("Category")


    @classmethod
    def get_all(cls):
        """Return all products from the database."""
        return cls.query.all()

    @classmethod
    def count_products(cls):
        """Return the total count of products."""
        return cls.query.count()
    
    def __repr__(self):
        return f'<Product {self.name}>'