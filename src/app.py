import os
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Получаем абсолютный путь к текущему скрипту
        script_dir = os.path.dirname(__file__)
        # Объединяем его с именем файла contacts.html
        file_path = os.path.join(script_dir, 'contacts.html')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Открываем и считываем содержимое файла contacts.html
        try:
            with open(file_path, 'rb') as file:
                self.wfile.write(file.read())
        except FileNotFoundError:
            # Если файл не найден, отправляем сообщение об ошибке
            self.send_error(404, "File not found")


# Запускаем сервер
if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Сервер запущен на http://localhost:8000')
    httpd.serve_forever()
