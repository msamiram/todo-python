from flask import Flask
from extensions import db, jwt
from config import Config
from flask_cors import CORS
from flask_migrate import Migrate

from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from routes.user_routes import user_bp
from routes.static_routes import static_bp
from dotenv import load_dotenv
load_dotenv()

migrate = Migrate()  

def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)

    CORS(app, origins=["http://127.0.0.1:5000", "http://localhost:5000"])

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)  

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(static_bp)

    @app.cli.command('init-db')
    def init_db():
        """Run database migrations."""
        from flask_migrate import upgrade
        upgrade()
        print("Database migrated to latest version.")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
