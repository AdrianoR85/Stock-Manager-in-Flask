from extensions import db

class Role(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(40), unique=True, nullable=True)

  def __repr__(self):
    return self.name