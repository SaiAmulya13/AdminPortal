from flask import Blueprint, request, jsonify
from ..models import Opportunity
from ..extensions import db

opp_bp = Blueprint("opp", __name__)


@opp_bp.route("/opportunities/<int:admin_id>", methods=["GET"])
def get_opportunities(admin_id):
    opps = Opportunity.query.filter_by(admin_id=admin_id).all()

    return jsonify([
        {
            "id": o.id,
            "name": o.name,
            "category": o.category,
            "duration": o.duration,
            "start_date": o.start_date,
            "description": o.description,
            "skills": o.skills,
            "future_opportunities": o.future_opportunities,
            "max_applicants": o.max_applicants
        }
        for o in opps
    ])


@opp_bp.route("/opportunity", methods=["POST"])
def add_opportunity():
    data = request.json
    opp = Opportunity(**data)
    db.session.add(opp)
    db.session.commit()
    return jsonify({"message": "Added"})


@opp_bp.route("/opportunity/<int:id>", methods=["PUT"])
def update_opportunity(id):
    opp = db.session.get(Opportunity, id)

    for key, value in request.json.items():
        setattr(opp, key, value)

    db.session.commit()
    return jsonify({"message": "Updated"})


@opp_bp.route("/opportunity/<int:id>", methods=["DELETE"])
def delete_opportunity(id):
    opp = db.session.get(Opportunity, id)
    db.session.delete(opp)
    db.session.commit()
    return jsonify({"message": "Deleted"})