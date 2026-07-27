import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

SERVER_URL = "http://127.0.0.1:8080/mcp"


def send_prompt(prompt: str) -> dict:
    payload = json.dumps({"prompt": prompt}).encode("utf-8")
    request = Request(SERVER_URL, data=payload, headers={"Content-Type": "application/json; charset=utf-8"})

    try:
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        return json.loads(response_body)
    except HTTPError as exc:
        return {"error": f"HTTP error {exc.code}: {exc.reason}"}
    except URLError as exc:
        return {"error": f"Bağlantı hatası: {exc.reason}"}


if __name__ == "__main__":
    prompt = "Merhaba MCP sunucusu"
    result = send_prompt(prompt)
    print(json.dumps(result, ensure_ascii=False, indent=2))
