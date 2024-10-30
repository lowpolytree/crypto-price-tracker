from flask import Flask

def create_app():
    app = Flask(__name__)
    print("Flask app initialized")
    
    #Import and register routes blueprint
    from .routes import main as main_bp
    app.register_blueprint(main_bp)
    
    return app