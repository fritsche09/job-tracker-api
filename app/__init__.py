from flask import Flask
from app.extensions import db
from app.models.job import Job # noqa: F401 - imported to register model with SQLAlchemy
from app.routes.jobs import jobs_bp

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///jobtracker.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        return {"message": "Job Tracker API is running"}
    
    app.register_blueprint(jobs_bp)
    
    return app