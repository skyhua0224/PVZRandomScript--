import keyboard
import threading
from game_operations import *
import interactive_menu

def run_game():
    LaunchGame()
    SelectGameMode("生存模式")
    SelectLevel()#自带等待加载
    SelectPlants()
    ReopenWindow(Tool)
    ExecuteScript(4)
    CloseWindow(Tool)
    TopWindow(Game)

def wait_and_run():
    if(CheckWindowIsOpen(Game) == False):
        return
    else:
        TopWindow(Game)
    time.sleep(5)
    SelectPlants()
    ReopenWindow(Tool)
    ExecuteScript(4)
    CloseWindow(Tool)
    TopWindow(Game)

def return_to_menu():
    interactive_menu.return_to_menu = True
    time.sleep(1)
    threading.Thread(target=interactive_menu.main).start()

if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+1', run_game)
    keyboard.add_hotkey('ctrl+2', wait_and_run)
    keyboard.add_hotkey('ctrl+0', return_to_menu)
    keyboard.wait()