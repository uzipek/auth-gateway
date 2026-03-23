import os
import sys
import logging
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from auth_gateway.config import config
from auth_gateway.auth import AuthManager

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    load_dotenv()

    auth_manager = AuthManager(app.config['AUTH_MANAGER'])
    auth_manager.init_app(app)

    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        user = auth_manager.authenticate(data['username'], data['password'])
        if user:
            token = auth_manager.generate_token(user.id)
            return jsonify({'token': token}), 200
        return jsonify({'error': 'Invalid credentials'}), 401

    @app.route('/protected', methods=['GET'])
    @auth_manager.login_required
    def protected():
        return jsonify({'message': 'Hello, authenticated user!'}), 200

    return app

if __name__ == '__main__':
    config_name = os.environ.get('CONFIG_NAME', 'development')
    app = create_app(config_name)
    app.run(debug=True)