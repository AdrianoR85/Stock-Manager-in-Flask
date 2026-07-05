from app.extensions import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    description = db.Column(db.Text(), nullable=True)
    
    @classmethod
    def count_categories(cls):
        return cls.query.count()

    def __repr__(self):
        return self.name