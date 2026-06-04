import requests

import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]

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
        f"https://api.telegram.org/bot8816834202:AAHKy3lpKXN7CUU6kVPR1RKAG9xwI-XY03Y/sendMessage",
        data={
            "chat_id": chat_id,
            "text": MESSAGE
        }
    )

print("Wiadomości wysłane")
