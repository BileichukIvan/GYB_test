from flask import Blueprint, request, jsonify
from app.models import User, db
from app.schemas import user_schema, users_schema
from flasgger import swag_from
from app.docs.user_docs import *

user_blueprint = Blueprint("users", __name__)


@user_blueprint.route("/users", methods=["POST"])
@swag_from(create_user_doc)
def create_user():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user), 201


@user_blueprint.route("/users", methods=["GET"])
@swag_from(get_users_doc)
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)


@user_blueprint.route("/users/<int:id>", methods=["GET"])
@swag_from(get_user_doc)
def get_user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)


@user_blueprint.route("/users/<int:id>", methods=["PUT"])
@swag_from(update_user_doc)
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json
    user.name = data.get("name", user.name)
    user.email = data.get("email", user.email)
    db.session.commit()
    return user_schema.jsonify(user)


@user_blueprint.route("/users/<int:id>", methods=["DELETE"])
@swag_from(delete_user_doc)
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})
