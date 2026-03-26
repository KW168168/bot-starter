import requests

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


def send_message(text: str) -> None:
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
"chat_id": CHAT_ID,
"text": text,
}

response = requests.post(url, json=payload, timeout=15)
response.raise_for_status()
print("Message sent successfully.")


if __name__ == "__main__":
send_message("Hello from bot-starter")
