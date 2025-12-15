# auth-gateway
# ===========

"""
Auth Gateway
------------

A simple authentication gateway service.

Dependencies
------------

* Flask
* Flask-JWT-Extended
* PyJWT
* SQLAlchemy

Installation
------------

To install the required dependencies, run:

pip install -r requirements.txt

Configuration
------------

You can configure the service by creating a `config.py` file in the root directory.
This file should contain the following settings:

```python
class Config:
    SECRET_KEY = 'your-secret-key'
    JWT_SECRET_KEY = 'your-jwt-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///auth-gateway.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Usage
-----

To run the service, execute:

python app.py

API Endpoints
------------

* `/login`: Handles user authentication.
* `/protected`: Requires authentication to access.
* `/logout`: Handles user logout.

Endpoints
---------

### Login

* `POST /login`

```json
{
  "username": "your-username",
  "password": "your-password"
}
```

* `application/json`
* `Content-Type: application/json`

### Protected

* `GET /protected`

```bash
{
  "message": "You are authenticated!"
}
```

### Logout

* `POST /logout`

```bash
{
  "message": "You have been logged out!"
}
```

API Documentation
--------------

You can generate API documentation using Swagger UI by running:

python -m flask run --host=0.0.0.0 --port=5000
```

```python
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)
db = SQLAlchemy(app)

from auth_gateway.models import User
from auth_gateway.routes import login, protected, logout

app.register_blueprint(login)
app.register_blueprint(protected)
app.register_blueprint(logout)

if __name__ == '__main__':
    app.run(debug=True)