import sys, time, os

def m(s, delay=0.05):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

# Bersihkan layar
os.system("clear")

# Banner Fall Bot
print("""
\033[1;31m
╔═╗┌─┐┬  ┬  ┌┐ ─  ┌┐┌┌─┐┌┬┐
║  │ ││  │  ├┴┐───││││ │ ││
╚═╝└─┘┴─┘┴─┘└─┘   ┘└┘└─┘─┴┘

███████╗░█████╗░██╗░░░░░██╗░░░░░
██╔════╝██╔══██╗██║░░░░░██║░░░░░
█████╗░░██║░░██║██║░░░░░██║░░░░░
██╔══╝░░██║░░██║██║░░░░░██║░░░░░
██║░░░░░╚█████╔╝███████╗███████╗
╚═╝░░░░░░╚════╝░╚══════╝╚══════╝
      \033[0;37;41m  TELEGRAM BOT XyzFalll  \033[0m
""")

m("\033[1;32m[+] Install bahan otomatis...\033[0m")
m("\033[1;33m[!] Jangan keluar dari Termux sebelum selesai!\033[0m\n")

# Instalasi otomatis
os.system("pkg update -y && pkg upgrade -y")
os.system("pkg install -y nano python python2 nodejs libwebp ffmpeg")
os.system("npm install")
os.system("npm audit fix --force")
os.system("npm install axios telegraf")

# Jalankan bot
m("\n\033[1;34m[•] Memulai Telegram Bot...\033[0m")
time.sleep(1)
os.system("clear")
os.system("python start.py")

m("\033[1;32mDONE BANG FALL!? 🚀 BOT SUDAH JALAN!\033[0m")