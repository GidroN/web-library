from flask import Flask, render_template, request
from database import init_app, db
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


app = Flask(__name__)
init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    logger.info('registry method called')

    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    is_admin = role == 'admin'

    user = User.query.filter_by(username=username).first()
    if user:
        logger.error(f'User {username} already exists')
        return 'Пользователь с таким именем уже существует.'

    logger.info('Creating new user..')
    new_user = User(username=username, password=generate_password_hash(password, method='sha256'), is_admin=is_admin)

    db.session.add(new_user)
    db.session.commit()

    if new_user.is_admin:
        logger.info(f'New admin registered {username}')
    else:
        logger.info(f'New user registered {username}')

    logger.info(f'Password {password}')
    logger.info(f'Role {role}')

    return f'Регистрация прошла успешно! Пользователь {username} с ролью {role} зарегистрирован.'

@app.route('/login', methods=['POST'])
def login():
    logger.info('login method called')

    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        logger.error(f'Incorrect input for username or password')
        return 'Неправильное имя пользователя или пароль.'

    if user.is_admin:
        logger.info(f'Admin login was successfully')
    else:
        logger.info(f'User login was successfully')

    logger.info(f'User {username}')
    logger.info(f'Password {password}')
    logger.info(f'Role {role}')


    if user.is_admin:
        return f"Добро пожаловать админ {username}"
    else:
        return f"Добро пожаловать библиотекарь {username}"


if __name__ == '__main__':
    app.run()
