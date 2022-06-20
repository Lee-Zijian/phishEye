import os
try:
    import colorama
except:    
    print("Some modules are not installed!!\nPlease wait. Installing.......")
    os.system('pip install colorama --quiet')
    os.system('cls' if os.name == 'nt' else 'clear')

from colorama import Fore, Style
import os
import time



def PrintBanner():
    print('''
    {bright}PhishTest Version {green}{ver}\t\tBy: {yellow}Zijian Li{white}
    '''.format(ver=1.0, red=Fore.RED, yellow=Fore.YELLOW, green=Fore.GREEN,
    blue=Fore.BLUE, pink=Fore.MAGENTA, white=Fore.WHITE, reset=Style.RESET_ALL, bright=Style.BRIGHT))

    time.sleep(2) 

# PrintBanner()
