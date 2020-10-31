from datetime import datetime
from core.database import db

class BaseModel():
    """ Generalize __init__, __repr__ and to_json
        Based on the models columns """

    _created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    _updated_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.now)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()