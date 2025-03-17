from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from app.models import User, db
from app.schemas import user_schema, users_schema
from flasgger import swag_from
from app.docs.user_docs import (
    update_user_doc,
    create_user_doc,
    delete_user_doc,
    get_user_doc,
    get_users_doc,
)

user_blueprint = Blueprint("users", __name__)


@user_blueprint.route("/users", methods=["POST"])
@swag_from(create_user_doc)
def create_user():
    try:
        data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    if User.query.filter_by(email=data.email).first():
        return jsonify({"error": {"email": ["Email already exists."]}}), 400

    new_user = User(name=data["name"], email=data["email"])
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
    try:
        data = user_schema.load(request.json, partial=True)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    user = User.query.get_or_404(id)

    if hasattr(data, "email") and data.email != user.email:
        if User.query.filter(User.email == data.email).first():
            return jsonify({"error": {"email": ["Email already exists."]}}), 400

    user.name = getattr(data, "name", user.name)
    user.email = getattr(data, "email", user.email)
    db.session.commit()

    return user_schema.jsonify(user), 200


@user_blueprint.route("/users/<int:id>", methods=["DELETE"])
@swag_from(delete_user_doc)
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})
