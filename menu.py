import colorama
from colorama import init, Fore, Back, Style
init()
def value():
    print(Fore.GREEN,Style.BRIGHT+ "Developer Toolkit" + Style.RESET_ALL)
    print("Please select an option ")
    print(Fore.BLUE,Style.NORMAL +"1.Notes\n 2.Tasks\n 3.Exit" + Style.RESET_ALL)
    n=int(input(""))
    return n
