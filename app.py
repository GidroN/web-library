from source.routes import app
from source.database import init_app

init_app(app)

if __name__ == '__main__':
    app.run(debug=True)