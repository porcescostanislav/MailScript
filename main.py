import random
import smtplib
from email.message import EmailMessage
import os
from time import sleep

# --- CONFIGURARE DATE ---
SENDER_EMAIL = os.environ.get("SENDER_EMAIL").strip()
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD").strip()

# --- RECEIVER EMAILS ---
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL").strip()

# ❤️ 💋 😘 💖
messages = [
    "Bună dimineața ❤️\nChiar dacă ne despart mulți kilometri, ești primul meu gând când mă trezesc. Te iubesc mult ❤️💋",
    "Bună dimineața 😘\nSper ca ziua ta să fie la fel de frumoasă ca zâmbetul tău. Abia aștept să ne revedem ❤️💋",
    "Bună dimineața frumoaso\nNu uita că ești puternică și că poți face față oricărei provocări azi. Mă mândresc cu tine 💋❤️",
    "Bună dimineața negila mea ❤️\nMi-aș fi dorit să fiu lângă tine acum să îți dau un pup, dar până atunci, îți transmit toată dragostea mea prin acest mesaj 💋❤️",
    "Distanța e doar un număr când inima mea e mereu la tine ❤️\nSă ai o zi productivă și plină de bucurii drăguț-o 💋❤️",
    "Zâmbește nigga 💋\nLumea e mai frumoasă când ești fericită. Te îmbrățișez strâns 💋💖",
    "Fiecare dimineață e mai bună pentru că știu că te am pe tine în viața mea. Te iubesc și abia aștept să te strâng în brațe 💖❤️"
]

# --- CREAREA MESAJULUI ---
msg = EmailMessage()
msg['Subject'] = f"Morning letter ❤️💋"
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg.set_content(random.choice(messages))

# --- TRIMITEREA ---
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("Autentificare...")
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()
    print("✅ SUCCES! Email-ul a fost trimis.")
except Exception as e:
    print(f"❌ Eroarea este: {e}")