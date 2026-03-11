from app.extensions import db
from datetime import date

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="applied")
    applied_date = db.Column(db.Date, default=date.today)
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Job {self.company} - {self.role}>"