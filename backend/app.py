from flask import Flask
from backend.routes.product_routes import product_bp
from backend.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(product_bp, url_prefix="/products")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)