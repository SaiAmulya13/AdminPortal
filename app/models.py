from .extensions import db, login_manager
from flask_login import UserMixin

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(200))

class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    duration = db.Column(db.String(50))
    start_date = db.Column(db.String(50))
    description = db.Column(db.Text)
    skills = db.Column(db.Text)
    category = db.Column(db.String(50))
    future_opportunities = db.Column(db.Text)
    max_applicants = db.Column(db.Integer)
    admin_id = db.Column(db.Integer)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))