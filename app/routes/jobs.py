from flask import Blueprint, request
from app.models.job import Job
from app.extensions import db


jobs_bp = Blueprint("jobs", __name__)

@jobs_bp.route("/jobs", methods=["GET"])
def get_jobs():
    all_jobs = Job.query.all()
    result = [{"id": job.id,"company": job.company,"role": job.role,"status": job.status,"applied_date": str(job.applied_date),"notes": job.notes} for job in all_jobs]
    
    return result, 200

@jobs_bp.route("/jobs/<id>", methods=["GET"])
def get_job(id):
    result = db.session.get(Job, id)
    if result:
        return {
            "id": result.id,
            "company": result.company,
            "role": result.role,
            "status": result.status,
            "applied_date": str(result.applied_date),
            "notes": result.notes
        }, 200
    
    return {"error": "Job not found"}, 404

@jobs_bp.route("/jobs", methods=["POST"])
def post_jobs():
    new_job = request.get_json()
    job_object = Job(
        company=new_job["company"],
        role=new_job["role"],
        status=new_job["status"],
        notes=new_job["notes"]
    )

    db.session.add(job_object)
    db.session.commit()
    return {"message": "Job has been posted"}, 201

@jobs_bp.route("/jobs/<id>", methods=["PUT"])
def update_jobs(id):
    updated_job = request.get_json()
    current_job = db.session.get(Job, id)
    
    if not current_job:
        return {"error": "Job not found"}, 404
    
    for key, value in updated_job.items():
        setattr(current_job, key, value)

    db.session.commit()
    
    return {
        "id": current_job.id,
        "company": current_job.company,
        "role": current_job.role,
        "status": current_job.status,
        "applied_date": str(current_job.applied_date),
        "notes": current_job.notes
    }, 200

@jobs_bp.route("/jobs/<id>", methods=["DELETE"])
def delete_job(id):
    job_to_delete = db.session.get(Job, id)

    if not job_to_delete:
        return {"message": "No job to delete or job doesn't exist"}, 404
    
    db.session.delete(job_to_delete)
    db.session.commit()

    return "", 204

    


