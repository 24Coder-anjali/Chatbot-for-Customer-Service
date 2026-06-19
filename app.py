import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from chatbot import CustomerServiceBot


BASE_DIR = Path(__file__).resolve().parent
bot = CustomerServiceBot()


class ChatbotRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR / "static"), **kwargs)

    def do_POST(self):
        if self.path != "/chat":
            self.send_error(404, "Endpoint not found")
            return

        content_length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(content_length)

        try:
            payload = json.loads(raw_body.decode("utf-8"))
            message = payload.get("message", "")
            response = bot.get_response(message)
            self._send_json(response)
        except json.JSONDecodeError:
            self._send_json({"reply": "Invalid request format.", "intent": "error", "confidence": 0}, status=400)

    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    port = 8000
    server = ThreadingHTTPServer(("localhost", port), ChatbotRequestHandler)
    print(f"Chatbot is running at http://localhost:{port}")
    print("Press Ctrl+C to stop the server.")
    server.serve_forever()


if __name__ == "__main__":
    main()
