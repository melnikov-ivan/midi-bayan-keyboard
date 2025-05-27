import board
import socketpool
import wifi
import gc
from adafruit_httpserver import Server, Request, Response, Middleware, serve_forever

# Подключение к WiFi (укажите название и пароль вашей сети)
wifi.radio.connect("YourNetworkName", "YourPassword")

# Создание объекта socketpool (для управления сетевыми соединениями)
pool = socketpool.SocketPool(wifi.radio)

# Создание экземпляра HTTP-сервера
server = Server(pool, "/static")

# Пример маршрута для GET запроса
@server.route("/hello", method=Request.GET)
def hello_get(request: Request):
    gc.collect()  # сборка мусора
    return Response(request, "Hello, Adafruit HTTP Server!", content_type="text/html")

# Пример маршрута для POST запроса
@server.route("/echo", method=Request.POST)
def echo(request: Request):
    gc.collect()  # сборка мусора
    request_headers = ",\n".join(f"{k}: {v}" for k, v in request.headers.items())
    return Response(
        request,
        f"Received POST request with headers:\n{request_headers}\n\nBody: {request.body.decode()}",
        content_type="text/plain"
    )

# Пример использования Middleware для логирования всех запросов
class LoggingMiddleware(Middleware):
    def process_request(self, request: Request) -> Request:
        print(f"Received request: {request.method} {request.url}")
        return request

server.add_middleware(LoggingMiddleware)

# Запуск сервера
serve_forever(server)