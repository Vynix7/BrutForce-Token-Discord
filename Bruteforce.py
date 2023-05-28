import base64, string, random
import colorama
from clear_screen import clear

def token_bruteforcer():
    try:
        clear()

        print("")
        print(colorama.Fore.LIGHTYELLOW_EX + "  /$$$$$$$  /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$")
        print(" | $$__  $$| $$__  $$| $$  | $$|__  $$__/| $$_____/| $$_____//$$__  $$| $$__  $$ /$$__  $$| $$_____/")
        print(" | $$  \ $$| $$  \ $$| $$  | $$   | $$   | $$      | $$     | $$  \ $$| $$  \ $$| $$  \__/| $$      ")
        print(" | $$$$$$$ | $$$$$$$/| $$  | $$   | $$   | $$$$$   | $$$$$  | $$  | $$| $$$$$$$/| $$      | $$$$$   ")
        print(colorama.Fore.LIGHTWHITE_EX + " | $$__  $$| $$__  $$| $$  | $$   | $$   | $$__/   | $$__/  | $$  | $$| $$__  $$| $$      | $$__/   ")
        print(" | $$  \ $$| $$  \ $$| $$  | $$   | $$   | $$      | $$     | $$  | $$| $$  \ $$| $$    $$| $$      ")
        print(" | $$$$$$$/| $$  | $$|  $$$$$$/   | $$   | $$$$$$$$| $$     |  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$$")
        print(" |_______/ |__/  |__/ \______/    |__/   |________/|__/      \______/ |__/  |__/ \______/ |________/")
        print(colorama.Fore.YELLOW + "")
                                                                                                   

        uuid = str(input('Used ID to bruteforce: '))
        if uuid == ''.strip():
            input('UUID cannot be empty, press enter to return ')
            token_bruteforcer()

        first_half = base64.b64encode(uuid.encode('utf-8')).decode().rstrip('b"')
        tried = set()
        amount = 0

        while True:
            second_half = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            third_half = ''.join(random.choice('-' + '_' + string.ascii_letters + string.digits) for _ in range(38))
            
            first_second_third = f'{first_half}.{second_half}.{third_half}'

            if first_second_third not in tried:
                tried.add(first_second_third)
                amount +=1
                print(f'{first_second_third} | {amount}')
                with open('tokens.txt', 'a') as tokens:
                    tokens.write(f'{first_second_third}\n')


    except KeyboardInterrupt:
        token_bruteforcer()

token_bruteforcer()