import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class MCPRequestHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/mcp":
            self._send_json({"error": "Beklenen yol /mcp"}, status=404)
            return

        content_length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(content_length).decode("utf-8")

        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            self._send_json({"error": "JSON çözümlenemedi"}, status=400)
            return

        prompt = payload.get("prompt", "")
        response = {
            "response": f"Merhaba! MCP sunucusu isteğinizi aldı.",
            "prompt": prompt,
            "tool_output": {
                "echo": prompt,
                "length": len(prompt),
            },
        }

        self._send_json(response)

if __name__ == "__main__":
    server_address = ("127.0.0.1", 8080)
    print("MCP sunucusu başlatılıyor: http://127.0.0.1:8080/mcp")
    HTTPServer(server_address, MCPRequestHandler).serve_forever()
