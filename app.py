from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')

    # Здесь вы можете добавить логику для обработки регистрации пользователя
    # Выводите значения username, password и role для просмотра

    print(f'Зарегистрирован пользователь: {username}')
    print(f'Пароль: {password}')
    print(f'Роль: {role}')

    # Возвращаем сообщение о успешной регистрации
    return f'Регистрация прошла успешно! Пользователь {username} с ролью {role} зарегистрирован.'

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')

    # Здесь вы можете добавить логику для обработки входа пользователя
    # Проверяйте соответствие введенного логина, пароля и роли с вашей системой аутентификации

    if username == 'admin' and password == 'admin123' and role == 'admin':
        return f'Добро пожаловать, администратор {username}!'
    elif username == 'librarian' and password == 'librarian123' and role == 'librarian':
        return f'Добро пожаловать, библиотекарь {username}!'
    else:
        return 'Ошибка: неправильные учетные данные или выбрана неправильная роль'


if __name__ == '__main__':
    app.run()
