from pywinauto.application import Application
from ctypes import *
import pyautogui
import subprocess
import time
import os
import win32gui
import win32con
import pyautogui

import keyboard
#自写脚本调用

#键盘事件初始化
print(1)

def m_KeyPressAction(key):
    match key:
        case 'Ctrl+1':
            print(key)

class KeyboardEvent(): 
    def __init__(self):
        self.KeyPress()

    def KeyPress(self):
        print(123)
        #快捷键
        KeyPressActions={'Ctrl+1','Ctrl+2','Ctrl+3','Ctrl+4','Ctrl+5','Ctrl+6','Ctrl+7','Ctrl+8','Ctrl+9'}

        for item in KeyPressActions:
            keyboard.add_hotkey(item, m_KeyPressAction, args=(item,))

    def KeyboardWait(self):
        print("已开启阻塞 脚本保持运行")
        keyboard.wait()

def Init():
    KeyboardEvent()

#main全部初始化
Init()




class Tool:
    name = '植物大战僵尸全版本辅助工具'
    path = r"C:\Users\XuanMeng\Desktop\plants\PvZ_Toolkit_v1.20.3\PvZ_Toolkit_v1.20.3.exe"
    hwnd = None
    left, top, right, bottom = None,None,None,None
    def ClearData():
        hwnd = None
        left, top, right, bottom = None,None,None,None

class Game:
    name = '植物大战僵尸中文版'
    path = r"C:\Users\XuanMeng\Desktop\plants\随机版各种版本\只有模仿者能随机的随机模仿者\模仿者随机版\PlantsVsZombies.exe"
    hwnd = None
    def ClearData():
        hwnd = None

commandDic = {'启动游戏' : 1, '应总选卡' : 2, '下一局' : 3}

#置顶窗口
def TopWindow(object):
    if object.hwnd:
        try:
            win32gui.ShowWindow(object.hwnd, win32con.SW_SHOWNORMAL)
        except:  
            app = Application().connect(path = object.path)
            app.top_window().set_focus()

#关闭窗口
def CloseWindow(object):
    if object.hwnd:
        win32gui.PostMessage(object.hwnd, win32con.WM_CLOSE, 0, 0)
        object.ClearData()
        time.sleep(1)
        print(Tool.name)
        print(Tool.hwnd)

#选植物
def SelectPlants():
    #TODO 修改前四个植物卡牌 从三发舍射手开始
    #模仿者
    pyautogui.click(1000, 900, clicks=1, interval=0.0, button='left')
    pyautogui.click(900, 900, clicks=1, interval=0.0, button='left')
    pyautogui.click(800, 900, clicks=1, interval=0.0, button='left')
    pyautogui.click(710, 900, clicks=1, interval=0.0, button='left')
    #普通卡牌
    pyautogui.click(700, 530, clicks=1, interval=0.0, button='left')
    pyautogui.click(420, 520, clicks=1, interval=0.0, button='left')
    pyautogui.click(1000, 530, clicks=1, interval=0.0, button='left')
    #小黑豆
    pyautogui.click(326, 530, clicks=1, interval=0.0, button='left')
    #禁用卡牌
    pyautogui.click(420, 780, clicks=1, interval=0.0, button='left')
    pyautogui.click(610, 790, clicks=1, interval=0.0, button='left')

def ToolPanelClick(x,y):
    pyautogui.click(Tool.left + x, Tool.top + y, clicks=1, interval=0.0, button='left')

#执行脚本
def ExecuteScript(cycleCount):
    ToolPanelClick(145,68)#点击阵型
    time.sleep(0.1)
    ToolPanelClick(84,120)#开选择卡槽
    time.sleep(0.1)
    ToolPanelClick(83,147)#第二卡槽
    time.sleep(0.1)
    ToolPanelClick(84,120)#开选择卡槽
    time.sleep(0.1)
    ToolPanelClick(82,95)#第一卡槽
    time.sleep(0.1)
    #换模仿者 
    while cycleCount:
        ToolPanelClick(465,122)#模仿者
        ToolPanelClick(237,120)#选择植物
        #滚动植物界面
        for i in range(0, 17):
            pyautogui.moveTo(237 + Tool.left, 0, 0.00001)#到最上
            pyautogui.moveTo(237 + Tool.left, 15)#到下面一点
        pyautogui.click(237 + Tool.left, 241, clicks=1, interval=0.0, button='left')#选择植物(小喷菇)
        ToolPanelClick(397,118)#换卡牌 确认
        time.sleep(0.01)
        if cycleCount!=1:
            #下一卡槽
            ToolPanelClick(84,120)
            ToolPanelClick(83,147)
        cycleCount-=1
    #双击快速布阵 刷新游戏中cd
    ToolPanelClick(102,161)
    time.sleep(0.2)
    ToolPanelClick(102,161)

#打开程序
def OpenWindow(object):
    subprocess.Popen(object.path, cwd = os.path.dirname(object.path))
    time.sleep(0.2)
    temphwnd = win32gui.FindWindow(None, object.name)
    time.sleep(0.2)
    if object.name == Game.name:
        Game.hwnd = temphwnd
    elif object.name == Tool.name:
        Tool.hwnd = temphwnd
        #获取窗口四角点位
        Tool.left, Tool.top, Tool.right, Tool.bottom = win32gui.GetWindowRect(Tool.hwnd)
        print(Tool.left)
        print(Tool.hwnd)

#检查程序是否开启
def CheckWindowIsOpen(object):
    temphwnd = win32gui.FindWindow(None, object.name)
    if temphwnd == 0:
        return False
    if object.name == Game.name:
        Game.hwnd = temphwnd
    elif object.name == Tool.name:
        Tool.hwnd = temphwnd
    time.sleep( 0.5)
    print(Game.hwnd)
    return True


print("""
请输入数字:
1.启动游戏
2.应总选卡
3.下一局
""")
command = int(input())

def LaunchGame():
    #等待游戏启动
    time.sleep(6)
    #点击开始
    pyautogui.click(972, 1000, clicks=1, interval=0.0, button='left')
    time.sleep(0.5)
    #打开关卡
    pyautogui.click(1220, 690, clicks=1, interval=0.0, button='left')#生存模式
    time.sleep(0.5)
    pyautogui.click(400, 570, clicks=1, interval=0.0, button='left')#选择关卡
    time.sleep(0.5)
    #上局游戏残留时点击新游戏
    pyautogui.click(1120, 660, clicks=1, interval=0.0, button='left')#新游戏
    pyautogui.click(790, 660, clicks=1, interval=0.0, button='left')#确定新游戏
    #等待场景动画
    time.sleep(5)

if command == commandDic['启动游戏']:
    if(CheckWindowIsOpen(Game) == False): #没打开程序
        OpenWindow(Game)
    else: #打开了程序
        CloseWindow(Game)
        time.sleep(1)
        OpenWindow(Game)
    LaunchGame()
    
elif command == commandDic['应总选卡']:
    if(CheckWindowIsOpen(Game) == False):
        OpenWindow(Game)
        LaunchGame()
    else:
        #游戏置顶
        TopWindow(Game)
        time.sleep(1)

elif command == commandDic['下一局']:
    if(CheckWindowIsOpen(Game) == False):
        OpenWindow(Game)
        LaunchGame()
    else:
        #游戏置顶
        TopWindow(Game)
        time.sleep(1)
    pyautogui.click(949, 709, clicks=1, interval=0.2, button='left')#重新开始
    time.sleep(5)

#选植物
SelectPlants()
time.sleep(0.5)
#点击开始按钮和未带阳光弹窗
pyautogui.click(660, 1020, clicks=1, interval=0.0, button='left')
pyautogui.click(660, 1020, clicks=1, interval=0.2, button='left')
pyautogui.click(790, 660, clicks=1, interval=0.2, button='left')
#等待场景动画
time.sleep(5)

CheckWindowIsOpen(Tool)
CloseWindow(Tool)
OpenWindow(Tool)
TopWindow(Tool)
time.sleep(0.1)

#执行脚本
ExecuteScript(4)
time.sleep(0.3)
CloseWindow(Tool)

#游戏置顶
TopWindow(Game)



KeyboardWait()