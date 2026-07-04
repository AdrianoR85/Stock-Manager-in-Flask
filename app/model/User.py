from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    last_updated = db.Column(db.DateTime(6), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    recovery_code = db.Column(db.String(200), nullable=True)
    active = db.Column(db.Boolean, default=1, nullable=True)

    role = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)

    funcao = db.relationship("Role")


    def _hash_password(self, password):
        return generate_password_hash(password)
    

    def set_password(self, password):
        self.password = self._hash_password(password)


    def verify_password(self, password):
        return check_password_hash(self.password, password)
        

    def __repr__(self):
        return f"{self.id} - {self.username}"