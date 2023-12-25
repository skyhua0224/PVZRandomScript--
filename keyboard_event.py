import keyboard
#自写脚本调用
from game_operations import *
import interactive_menu

class KeyboardEvent(): 
    def __init__(self):
        self.KeyPress()

    def KeyPress(self):
        #从data中获取快捷键
        KeyPressActions = {'Ctrl+1','Ctrl+2','Ctrl+3','Ctrl+4','Ctrl+5','Ctrl+6','Ctrl+7','Ctrl+8','Ctrl+9'}
        for item in KeyPressActions:
            keyboard.add_hotkey(item, self.KeyPressAction, args=(item,))
    #案件对应效果
    def KeyPressAction(self,key):
        match key:
            case 'Ctrl+1':
                #重启游戏..加载=>进入生存模式=>选择白天困难..加载=>选卡=>打开Tool=>脚本运行
                LaunchGame()
                SelectGameMode("生存模式")
                SelectLevel()#自带等待加载
                SelectPlants()
                ReopenWindow(Tool)
                ExecuteScript(4)
                CloseWindow(Tool)
                TopWindow(Game)
            case 'Ctrl+2':
                #等待=>选卡=>脚本运行
                if(CheckWindowIsOpen(Game) == False):
                    return
                else:
                    #游戏置顶
                    TopWindow(Game)
                time.sleep(5)
                SelectPlants()
                ReopenWindow(Tool)
                ExecuteScript(4)
                CloseWindow(Tool)
                TopWindow(Game)
            case 'Ctrl+3':
                interactive_menu.main()

    #持续等待键盘按键
    def KeyboardWait(self):
        print("已开启阻塞 脚本保持运行")
        keyboard.wait()