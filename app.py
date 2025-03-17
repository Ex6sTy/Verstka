from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Читаем HTML-файл
    with open('templates/contacts2.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    # Возвращаем HTML с правильным Content-Type
    return html_content, 200, {'Content-Type': 'text/html'}

@app.route('/submit', methods=['POST'])
def submit():
    # Получаем данные из формы
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Выводим данные в консоль
    print(f"Имя: {name}")
    print(f"Почта: {email}")
    print(f"Сообщение: {message}")

    # Возвращаем ответ
    return "Данные успешно получены!", 200

if __name__ == '__main__':
    app.run(debug=True)