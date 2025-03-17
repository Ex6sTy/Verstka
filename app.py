from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    # Читаем HTML-файл
    with open('templates/contacts2.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    # Возвращаем HTML с правильным Content-Type
    return html_content, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app.run(debug=True)