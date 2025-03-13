from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Открываем файл contacts.html и читаем его содержимое
        with open('contacts.html', 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Устанавливаем заголовок Content-type
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Отправляем содержимое файла
        self.wfile.write(html_content.encode('utf-8'))

    def do_POST(self):
        # Получаем длину данных
        content_length = int(self.headers['Content-Length'])
        # Читаем данные из запроса
        post_data = self.rfile.read(content_length)

        # Выводим данные в консоль
        print(f"Получены данные: {post_data.decode('utf-8')}")

        # Отправляем ответ
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'POST-запрос успешно обработан')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Сервер запущен на порту {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
