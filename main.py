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
    "Bună dimineața negrila mea ❤️\nMi-aș fi dorit să fiu lângă tine acum să îți dau un pup, dar până atunci, îți transmit toată dragostea mea prin acest mesaj 💋❤️",
    "Distanța e doar un număr când inima mea e mereu la tine ❤️\nSă ai o zi productivă și plină de bucurii drăguț-o 💋❤️",
    "Zâmbește nigga 💋\nLumea e mai frumoasă când ești fericită. Te îmbrățișez strâns 💋💖",
    "Fiecare dimineață e mai bună pentru că știu că te am pe tine în viața mea. Te iubesc și abia aștept să te strâng în brațe 💖❤️",
    "Bună dimineața! ☀️\nEști motivul pentru care adorm cu zâmbetul pe buze și mă trezesc cu speranță. Te ador! 💖",
    "Neața, raza mea de soare! ☀️\nChiar dacă ești departe, te simt aici, lângă inima mea. Să ai o zi frumoasa! ✨❤️",
    "Bună dimineața, iubito! ❤️\nÎți trimit o îmbrățișare virtuală atât de strânsă încât să o simți toată ziua. 💋",
    "Cea mai frumoasă parte a dimineții e să-ți scriu ție. 💌\nTe iubesc enorm, negrila mea! ❤️💋",
    "Bună dimineața! \nSper sa fii toata ziua cu gândul la mine, așa cum eu mă gândesc la tine cu fiecare respirație. Te pup! 😘",
    "O zi nouă, un nou motiv să-ți spun cât de mult însemni pentru mine. ❤️\nEști totul, frumoaso! 💋💖",
    "Bună dimineața, gorgeous ahh niga! ✨\nDistanta asta e temporară, dar iubirea noastră e pentru totdeauna. Ai grijă de tine azi! ❤️",
    "Neața, drăguț-o! 💖\nAbia aștept momentul în care n-o să mai fie nevoie să-ți scriu mesaje, ci să te sărut direct. 💋❤️",
    "Bună dimineața! 🌸\nEști cea mai puternică persoană pe care o cunosc. Arată-le tuturor cât de tare ești azi! 🔥❤️",
    "Zâmbește, nigga! ❤️\nO zi fără zâmbetul tău e o zi pierdută. Te iubesc până la lună și înapoi! 🌙✨",
    "Bună dimineața! ☀️\nMi-e dor de tine foarte mult dar gândul că ești a mea mă face cel mai fericit. 💋💖",
    "Sper ca acest mesaj să-ți aducă un zâmbet pe față de la prima oră. ☺️\nTe iubesc nespus, negrila mea! ❤️💋",
    "Bună dimineața, minunato! ✨\nEști dovada că distanța nu poate stinge o iubire adevărată. Să ai o zi plină de succes! 💪❤️",
    "Neața! \nÎți trimit un sărut pe frunte și multă energie pentru tot ce ai de făcut azi. Te pup! 💋❤️",
    "Bună dimineața, iubirea mea! ❤️\nEști visul din care nu vreau să mă trezesc niciodată. Te ador! 💖😘",
    "O dimineață superbă pentru o fată superbă! 🌸\nSă strălucești azi, așa cum strălucești mereu în ochii mei. 💋❤️",
    "Neața, frumoaso! ❤️\nNu uita să faci pauze, să bei apă și să te gândești puțin la mine. Te iubesc! 💋✨",
    "Bună dimineața! ✨\nInima mea bate în același ritm cu a ta, indiferent de câți kilometri sunt între noi. ❤️💖",
    "Zâmbește, drăguț-o! 😊\nAi o lume întreagă de cucerit azi, iar eu sunt aici să te susțin în tot. Te pup! 💋❤️",
    "Bună dimineața, negrila! ❤️\nEști cea mai mare binecuvântare din viața mea. Să ai o zi liniștită și frumoasă! 💋",
    "Neața! ☀️\nMă trezesc recunoscător pentru fiecare secundă în care te am în viața mea. Te iubesc mult! ❤️💖",
    "Bună dimineața! ✨\nEști prima și ultima mea dorință în fiecare zi. Abia aștept să te revăd! 💋❤️",
    "O zi minunată, iubito! ❤️\nFiecare pas pe care îl faci azi să te aducă mai aproape de visurile tale... și de mine. Te ador! 💖💋"
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