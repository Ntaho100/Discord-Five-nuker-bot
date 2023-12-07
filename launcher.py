import urllib.request
import shutil
import os
from pathlib import Path
import urllib3
from colorama import Fore
import colorama
from time import sleep
os.system("title Five Nuker - Launcher")
colorama.init(autoreset=True)

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def clear_installator():
    try:
        la = Path('installer.exe')
        if la.is_file:
            os.system('taskkill /f /im installer.exe')
            clear()
            os.remove('installer.exe')
    except: pass


clear_installator()


def remade_bin_folder():
    try:
        os.mkdir('Bin')
    except:
        shutil.rmtree('Bin')
        os.mkdir('Bin')

def move_stuff(type):
    if type == 'no':
        nuker = str(Path('fn.exe'))
        ver_file = str(Path('curent_version.fnv'))
        work_folder = str(os.getcwd())
        bin_folder = work_folder + '\Bin'
        shutil.move(nuker, bin_folder)
        shutil.move(ver_file, bin_folder)
    elif type == 'yes':
        icon = str(Path('icon.PNG'))
        nuker = str(Path('fn.exe'))
        ver_file = str(Path('curent_version.fnv'))
        work_folder = str(os.getcwd())
        bin_folder = work_folder + '\Bin'
        shutil.move(icon, bin_folder)
        shutil.move(nuker, bin_folder)
        shutil.move(ver_file, bin_folder)





http = urllib3.PoolManager()

get_launcher_last_ver = http.request('GET', 'https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/launcher_last_ver')
get_last_ver = http.request('GET', 'https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/curent_version.fnv')
get_changelog = http.request('GET', 'https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/nuker_changelog')
is_update_has_cfgsys_changes = http.request('GET', 'https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/is_update_has_cfgsys_changes')
get_last_ver = get_last_ver.data.decode('utf-8')
get_launcher_last_ver = get_launcher_last_ver.data.decode('utf-8')
get_changelog = get_changelog.data.decode('utf-8')
is_update_has_cfgsys_changes = is_update_has_cfgsys_changes.data.decode('utf-8')


curent_launcher_ver = str('4')
print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Checking for updates...')
if not get_launcher_last_ver == curent_launcher_ver:
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} New launcher version detected!')
    urllib.request.urlretrieve("https://github.com/glitch65/Discord-Five-nuker-bot/raw/launcher/installer.exe", "installer.exe")
    os.system('installer.exe')
else:
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Launcher does not require updating!')


def install_nuker():
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Installing nuker...')
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading fn.exe...')
    urllib.request.urlretrieve("https://github.com/glitch65/Discord-Five-nuker-bot/raw/launcher/five%20nuker.exe", "fn.exe")
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading curent_version.fnv...')
    urllib.request.urlretrieve("https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/curent_version.fnv", "curent_version.fnv")
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading icon.PNG...')
    urllib.request.urlretrieve("https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/main/icon.PNG", "icon.PNG")
    remade_bin_folder()
    move_stuff('yes')
    os.mkdir('Configs')
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Installed!')

def launch_nuker():
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Staring nuker...')
    os.system('Bin\\fn.exe')

def check_curent_n_install():
    try:
        curent_version = open('Bin\curent_version.fnv', 'r')
        curent_version = curent_version.read()
    except:
        install_nuker()
        launch_nuker()

check_curent_n_install()
curent_version = open('Bin\curent_version.fnv', 'r')
curent_version = curent_version.read()

if not os.path.exists('Configs'):
    os.mkdir('Configs')

def n_check():
    try:
        if curent_version == get_last_ver:
            print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Nuker does not require updating!')
            launch_nuker()
        else:
            show_nupdate_massage()
    except:
        print('An error occurred while checking for updates, to solve it, please notify me (the creator) in my discord server or create a issue in Github repository')
        input('Press Enter to close nuker...')
        quit()

def show_nupdate_massage():
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} New nuker {curent_version} -> {get_last_ver} version avaible!')
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Changelog:')
    print(get_changelog)
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} 1 - Install update | 2 - Ignore update and start nuker')
    user_choice = input(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Select >>> ')
    if user_choice == '1':
        update_nuker()
    elif user_choice == '2':
        launch_nuker()
    else:
        print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Please enter number 1 or 2!')
        sleep(2)
        clear()
        show_nupdate_massage()


def backup_user_files():
    icon = str(Path('Bin\icon.PNG'))
    work_folder = str(os.getcwd())
    shutil.move(icon, work_folder)

def restore_user_files():
    icon = str(Path('icon.PNG'))
    work_folder = str(os.getcwd())
    bin_folder = work_folder + '\\Bin'
    shutil.move(icon, bin_folder)

def update_nuker():
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Updating nuker...')
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading fn.exe...')
    urllib.request.urlretrieve("https://github.com/glitch65/Discord-Five-nuker-bot/raw/launcher/five%20nuker.exe", "fn.exe")
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Downloading curent_version.fnv...')
    urllib.request.urlretrieve("https://raw.githubusercontent.com/glitch65/Discord-Five-nuker-bot/launcher/curent_version.fnv", "curent_version.fnv")
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Backuping user files...')
    backup_user_files()
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Updating nuker...')
    remade_bin_folder()
    move_stuff('no')
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} restoring user files...')
    restore_user_files()
    print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} Done!')
    if is_update_has_cfgsys_changes == 'yes':
        print(f'{Fore.YELLOW}[Launcher]{Fore.RESET} New version of Five nuker contaians config system changes')
        print(f'{Fore.RED}[WARNING]{Fore.RESET} Your config will be deleted')
        input('Press Enter to delete config')
        os.remove('Configs\\main_cfg.ini')
        print('Config was succesfully deleted!')        
    launch_nuker()





n_check()
