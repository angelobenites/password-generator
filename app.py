import random
import string
import os
from colorama import Fore, Style, init

init(autoreset=True)

def generar_password(longitud):
     caracteres = string.ascii_letters + string.digits + string.punctuation
     password = "".join(random.choice(caracteres) for i in range(longitud))
     return password

while True:
     try:
          print("=============================")
          print(Style.BRIGHT + Fore.CYAN + """
          Ctrl + C para salir
          """)
          size = int(input("Logitud deseada para la contraseña: >_ "))
          print('Cargando...')
          os.system('cls' if os.name == 'nt' else 'clear')
          print(" ")
          print(Fore.GREEN + "--- PASSKEY ---")
          print(" ")
          print(Fore.GREEN + f"Tu nueva contraseña es: {generar_password(size)}")
     except KeyboardInterrupt:
          print(Fore.RED + "\nSaliendo...")
          break