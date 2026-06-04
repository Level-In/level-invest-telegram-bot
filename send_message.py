import os
import requests

print("TEST NOWEJ WERSJI")

TOKEN = os.environ["TELEGRAM_TOKEN"]

CHAT_IDS = [
    "-1004231126426",
    "-1004249984029",
    "-1003932802265"
]

MESSAGE = """Dziękujemy za dzisiejszy dzień! 💛

Wasza energia, zaangażowanie i każda aktywność naprawdę robią różnicę 💪✨

Przypominamy o aktualizacji aktywności do godziny 20:00 ⏰📲

Trzymamy tempo i działamy dalej! 🚀"""

for chat_id in CHAT_IDS:
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={
                "chat_id": chat_id,
                "text": MESSAGE
            },
            timeout=30
        )

        print(
            f"CHAT: {chat_id} | STATUS: {response.status_code} | ODPOWIEDŹ: {response.text}"
        )

    except Exception as e:
        print(f"BŁĄD DLA {chat_id}: {e}")

print("KONIEC PROGRAMU")
