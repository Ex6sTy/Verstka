from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    with open('index.html', 'r', encoding='utf-8') as file:
        content = file.read()
    return content, 200, {'Content-Type': 'text/html'}

@app.route('/contacts', methods=['GET'])
def contacts():
    with open('contacts.html', 'r', encoding='utf-8') as file:
        content = file.read()
    return content, 200, {'Content-Type': 'text/html'}

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    print("Полученные данные:", data)
    return "Данные получены", 200

if __name__ == '__main__':
    app.run(debug=True)