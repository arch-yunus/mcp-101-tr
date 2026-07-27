# 01-temeller

Bu bölümde MCP'nin temel kavramlarını öğreneceksiniz.

## Nedir?

Model Context Protocol (MCP), LLM'lerin dış dünyayla güvenli bir şekilde etkileşime geçmesini sağlar. Bu etkileşim genellikle:

- Yerel dosyalar
- Veritabanları
- Dış API'ler
- Sistem araçları

gibi kaynaklarla olur.

## Temel Bağlantılar

- `Client`: Yapay zekâ modelinden gelen istekleri gönderir.
- `Server`: Modelden gelen komutları çalıştırır ve sonuçları döndürür.

## Protokol Tipleri

- `stdio`: Standart giriş/çıkış üzerinden veri alışverişi.
- `SSE`: Sunucudan istemciye olay akışı.

## Nasıl Başlanır?

Bu rehberde her bölümde adım adım ilerleyecek, önce basit bir MCP sunucusu kuracak sonra araçlar ve kaynaklar ekleyeceğiz.
