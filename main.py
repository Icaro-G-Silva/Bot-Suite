from src.Interface import Interface
from src.modules.Colors import Colors

from time import sleep

try:
    interface = Interface()
    interface.menu()
except Exception as error:
    print(f'{Colors.FAIL}System non functional, an error has been occurred -> {error}{Colors.ENDC}')
finally:
    print(f'\n\n\n{Colors.HEADER}May the force be with you!{Colors.ENDC}')
    sleep(3)
