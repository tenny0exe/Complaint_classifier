from datetime import datetime
from .database import db

class Complaint(db.Model):
    __tablename__ = 'complaints'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Submitted')
    is_anonymous = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    forwarded_to_department = db.Column(db.Boolean, default=False)
    forwarded_at = db.Column(db.DateTime)
    department_response = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Complaint {self.id}>'