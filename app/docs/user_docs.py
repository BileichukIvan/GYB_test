# docs/user_docs.py

create_user_doc = {
    "tags": ["Users"],
    "summary": "Create a new user",
    "description": "Adds a new user to the database with a unique email.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "example": "John Doe"},
                    "email": {"type": "string", "example": "john.doe@example.com"},
                },
                "required": ["name", "email"],
            },
        }
    ],
    "responses": {
        201: {
            "description": "User created successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "John Doe"},
                    "email": {"type": "string", "example": "john.doe@example.com"},
                },
            },
        },
        400: {"description": "Invalid input"},
    },
}

get_users_doc = {
    "tags": ["Users"],
    "summary": "Retrieve all users",
    "description": "Returns a list of all registered users.",
    "responses": {
        200: {
            "description": "List of users",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer", "example": 1},
                        "name": {"type": "string", "example": "John Doe"},
                        "email": {"type": "string", "example": "john.doe@example.com"},
                    },
                },
            },
        }
    },
}

get_user_doc = {
    "tags": ["Users"],
    "summary": "Get user by ID",
    "description": "Retrieves a single user by their unique ID.",
    "parameters": [
        {"name": "id", "in": "path", "type": "integer", "required": True, "example": 1}
    ],
    "responses": {
        200: {
            "description": "User details",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "John Doe"},
                    "email": {"type": "string", "example": "john.doe@example.com"},
                },
            },
        },
        404: {"description": "User not found"},
    },
}

update_user_doc = {
    "tags": ["Users"],
    "summary": "Update user details",
    "description": "Updates an existing user’s name or email.",
    "parameters": [
        {"name": "id", "in": "path", "type": "integer", "required": True, "example": 1},
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "example": "Jane Doe"},
                    "email": {"type": "string", "example": "jane.doe@example.com"},
                },
            },
        },
    ],
    "responses": {
        200: {
            "description": "User updated successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer", "example": 1},
                    "name": {"type": "string", "example": "Jane Doe"},
                    "email": {"type": "string", "example": "jane.doe@example.com"},
                },
            },
        },
        404: {"description": "User not found"},
    },
}

delete_user_doc = {
    "tags": ["Users"],
    "summary": "Delete user",
    "description": "Removes a user from the database.",
    "parameters": [
        {"name": "id", "in": "path", "type": "integer", "required": True, "example": 1}
    ],
    "responses": {
        200: {
            "description": "User deleted successfully",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "User deleted successfully",
                    }
                },
            },
        },
        404: {"description": "User not found"},
    },
}
