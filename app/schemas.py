from app.extensions import ma, db
from app.models import User
from marshmallow import validate, ValidationError


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    name = ma.String(
        required=True,
        validate=[
            validate.Length(
                min=1, max=255, error="Name must be between 1 and 255 characters long."
            )
        ],
    )

    email = ma.String(
        required=True,
        validate=[
            validate.Length(
                min=1, max=255, error="Email must be between 1 and 255 characters long."
            ),
            validate.Email(error="Invalid email format."),
        ],
    )

    @staticmethod
    def validate_email(email):
        if db.session.query(User).filter(User.email == email).first():
            raise ValidationError("Email already exists.")

user_schema = UserSchema()
users_schema = UserSchema(many=True)
