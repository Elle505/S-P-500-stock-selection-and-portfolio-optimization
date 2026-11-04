# `.env` – API Kulcsok és Rendszerbeállítások


Ez a rejtett konfigurációs fájl tárolja a külső szolgáltatásokhoz (főképp az Alpaca API-hoz) szükséges elérési kulcsokat és beállításokat.

---

### 1. Alpaca API Kulcsok (`APCA_API_KEY_ID`, `APCA_API_SECRET_KEY`)
* Az Alpaca adatszolgáltató azonosítója és titkos kulcsa, amely a perces és napi árfolyamadatok letöltéséhez szükséges.

### 2. Adatfolyam Beállítása (`ALPACA_FEED`)
* Beállítja az Alpaca adatforrás típusát (`sip` / `iex`), ahonnan a perces részvényadatok érkeznek.
