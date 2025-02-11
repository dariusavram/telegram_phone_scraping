# Telegram Scraping Tool

## Descriere
Acest script extrage numerele de telefon și numele de utilizator ale participanților dintr-un grup Telegram utilizând biblioteca **Telethon**.

## Funcționalități
- **Autentificare cu Telegram** folosind API ID și API Hash.
- **Obținerea listei de participanți** dintr-un grup specificat.
- **Salvarea datelor** într-un fișier text, alegând dintre mai multe opțiuni:
  1. Numere de telefon.
  2. Nume de utilizator și numere de telefon.
  3. Ambele (în fișiere separate).
  4. Doar numele de utilizator.

## Cerințe
- **Python 3.x**
- **Biblioteca Telethon**, instalată cu:
  ```sh
  pip install telethon

## Configurare API Telegram
- **Obține API ID și API Hash:**  
  - [Accesează Telegram API](https://my.telegram.org/apps)
  - Creează o aplicație nouă și salvează API ID și API Hash.  
## Date necesare
- API ID și API Hash din Telegram.
- Numărul de telefon (inclusiv codul de țară, ex: +40...).
- Numele grupului Telegram (ex: t.me/numegrup).

## Rulare

```sh
python mybot.py
```
- Introdu datele cerute la rulare.
-  În funcție de alegerea utilizatorului, se salvează datele în fișiere .txt.

## Observații
- Scriptul necesită ca utilizatorul să fie membru al grupului pentru a extrage date.
- Telegram poate impune limitări asupra acestui script (după o anumită perioadă de utilizare, apare un cooldown).
