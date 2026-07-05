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


    @classmethod
    def _hash_password(cls, password):
        """Hash the password using Werkzeug's generate_password_hash."""
        return generate_password_hash(password)

    @classmethod
    def set_password(cls, user, password):
        user.password = cls._hash_password(password)

    @classmethod
    def verify_password(cls, user, password):
        """Verify the password using Werkzeug's check_password_hash."""
        return check_password_hash(user.password, password)

    @classmethod
    def count_users(cls):
        """Return the total count of users."""
        return cls.query.count()
    
    @classmethod
    def get_all_users(cls):
        """Return all users from the database."""
        return cls.query.all()

    @classmethod 
    def get_by_email(cls, email):
        """Return a user by email."""
        return cls.query.filter_by(email=email).first()

    def __repr__(self):
        return f"{self.id} - {self.username}"
    

