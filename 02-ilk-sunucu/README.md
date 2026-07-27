# 02-ilk-sunucu

Bu bölümde Python kullanarak basit bir MCP sunucusu yazıyoruz. Sunucu, `POST /mcp` yoluna gelen JSON istekleri kabul eder ve yanıt üretir.

## Çalıştırma

```powershell
python 02-ilk-sunucu/server.py
```

## Test

`curl` ile test edebilirsiniz:

```bash
curl -X POST http://localhost:8080/mcp -H "Content-Type: application/json" -d '{"prompt":"Merhaba MCP"}'
```
