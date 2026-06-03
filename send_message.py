import requests

TOKEN = "8816834202:AAGsK0NYDf3ju09wIg-lBC7WsShFhkbJ2WM"

CHAT_IDS = [
    "-1004231126426",  # GDAŃSK
    "-1004249984029",  # WARSZAWA
    "-1003932802265"   # KRAKÓW
]

MESSAGE = """Dziękujemy za dzisiejszy dzień! 💛

Wasza energia, zaangażowanie i każda aktywność naprawdę robią różnicę 💪✨

Przypominamy o aktualizacji aktywności do godziny 20:00 ⏰📲

Trzymamy tempo i działamy dalej! 🚀"""

for chat_id in CHAT_IDS:
    requests.post(
        f"https://api.telegram.org/bot8816834202:AAGsK0NYDf3ju09wIg-lBC7WsShFhkbJ2WM/sendMessage",
        data={
            "chat_id": chat_id,
            "text": MESSAGE
        }
    )

print("Wiadomości wysłane")
