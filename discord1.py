import os
import random
import string
import time
import ctypes
import colorama
# ! WARNING ! very unprofessional code up ahead, be weary 
try: 
    from discord_webhook import DiscordWebhook 
except ImportError:
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") 
    exit()
    # looking for webhook
try: 
    import requests 
except ImportError: 
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit() 


class NitroGen: 
    def __init__(self): 
        self.fileName = "codes.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt": 
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("nitro gen - made by sim-byte :)") 
        else:
            print(f'\33]0;nitro gen - made by sim-byte\a', end='', flush=True) 

        print(""" nitro generator """) 
        time.sleep(2) 
        self.slowType("made by sim-byte", .02) 
        time.sleep(1) 
        self.slowType("\n How many codes do you want to generate? : ", .02, newLine = False) 

        num = int(input('')) 

        self.slowType("\n Do you want to impliment a discord web hook? \n if you would like to, type it here or press enter to ignore: ", .02, newLine = False)
        url = input('') 
        webhook = url if url != "" else None 

        

        valid = []
        invalid = 0 

        for i in range(num): 
            try: 
                code = "".join(random.choices( 
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))

                url = f"https://discord.gift/{code}"  
                # you can use this code as a token creator by removing "https://discord.gift/" and changing some code on the top

                result = self.quickChecker(url, webhook)

                if result: 
                    valid.append(url)
                else: 
                    invalid += 1 
            except Exception as e: 
                print(f" Error | {url} ")

            if os.name == "nt": 
                ctypes.windll.kernel32.SetConsoleTitleW(f"nitro gen / checker - {len(valid)} Valid | {invalid} Invalid - made by sim-byte") 
                print("")
            else: 
                print(f'\33]0;nitro gen - {len(valid)} Valid | {invalid} Invalid - made by sim-byte\a', end='', flush=True) 

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") 

        input("\nThe end! Press Enter 5 times to close the program.") 
        [input(i) for i in range(4,0,-1)] 


    def slowType(self, text, speed, newLine = True): 
        for i in text:
            print(i, end = "", flush = True) 
            time.sleep(speed) 
        if newLine: 
            print() 
    def generator(self, amount): 
        with open(self.fileName, "w", encoding="utf-8") as file: 
            print("generating them rq, hold up") 

            start = time.time() 

            for i in range(amount): 
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) 

                file.write(f"https://discord.gift/{code}\n") 

            
            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): 
        valid = []
        invalid = 0 
        with open(self.fileName, "r", encoding="utf-8") as file: 
            for line in file.readlines(): 
                nitro = line.strip("\n") 

                
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200:
                    print(f"(Fore.GREEN) Valid | {nitro} ") 
                    valid.append(nitro) 

                    if notify is not None: 
                        DiscordWebhook( # sends message telling user there's a valid code
                            url = notify,
                            content = f"Nitro Grabbed :). (@everyone) \n{nitro}"
                        ).execute()
                    else: # if there hasn't been a discord webhook setup just stop the code
                        break 

                else:
                    print(f" Invalid | {nitro} ") 
                    invalid += 1 

        return {"valid" : valid, "invalid" : invalid} 

    def quickChecker(self, nitro, notify = None):
        
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200: 
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            with open("Nitro Codes.txt", "w") as file:
                file.write(nitro) 

            if notify is not None: 
                DiscordWebhook( 
                    url = notify,
                    content = f"Nitro Grabbed!.  (@everyone) \n{nitro}"
                ).execute()

            return True 

        else: 
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            return False 

if __name__ == '__main__':
    Gen = NitroGen() 
    Gen.main() 
