from ctypes import *
import pyautogui
import time
import pyautogui
import keyboard
#自写脚本调用
from WindowManager import *
from CommonData import *

def LaunchGame():
    ##打开游戏
    if(CheckWindowIsOpen(Game) == False): #没打开程序
        OpenWindow(Game)
    else: #打开了程序
        CloseWindow(Game)
        time.sleep(1)
        OpenWindow(Game)
    #等待游戏启动
    time.sleep(6)
    #点击开始
    pyautogui.click(972, 1000, clicks=1, interval=0.0, button='left')
    time.sleep(0.5)
    
def SelectGameMode():
    pyautogui.click(1220, 690, clicks=1, interval=0.0, button='left')#生存模式
    time.sleep(0.5)

def SelectLevel():
    pyautogui.click(400, 570, clicks=1, interval=0.0, button='left')#选择关卡
    time.sleep(0.5)
    #上局游戏残留时点击新游戏
    pyautogui.click(1120, 660, clicks=1, interval=0.0, button='left')#新游戏
    pyautogui.click(790, 660, clicks=1, interval=0.0, button='left')#确定新游戏
    #等待场景动画
    time.sleep(5)

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
    time.sleep(0.5)
    #点击开始按钮和未带阳光弹窗
    pyautogui.click(660, 1020, clicks=1, interval=0.0, button='left')
    pyautogui.click(660, 1020, clicks=1, interval=0.2, button='left')
    pyautogui.click(790, 660, clicks=1, interval=0.2, button='left')
    #等待场景动画
    time.sleep(4.5)

def WindowClick(object,x,y):#窗口的左上角(0,0)
    pyautogui.click(Tool.left + x, Tool.top + y, clicks=1, interval=0.0, button='left')

def ExecuteScript(cycleCount):
    WindowClick(Tool,145,68)#点击阵型
    time.sleep(0.1)
    WindowClick(Tool,84,120)#开选择卡槽
    time.sleep(0.1)
    WindowClick(Tool,83,147)#第二卡槽
    time.sleep(0.1)
    WindowClick(Tool,84,120)#开选择卡槽
    time.sleep(0.1)
    WindowClick(Tool,82,95)#第一卡槽
    time.sleep(0.1)
    #换模仿者 
    while cycleCount:
        WindowClick(Tool,465,122)#模仿者
        WindowClick(Tool,237,120)#选择植物
        #滚动植物界面
        for i in range(0, 18):
            pyautogui.moveTo(237 + Tool.left, 0, 0.00001)#到最上
            pyautogui.moveTo(237 + Tool.left, 15)#到下面一点
        pyautogui.click(237 + Tool.left, 241, clicks=1, interval=0.0, button='left')#选择植物(小喷菇)
        WindowClick(Tool,397,118)#换卡牌 确认
        time.sleep(0.01)
        if cycleCount!=1:
            #下一卡槽
            WindowClick(Tool,84,120)
            WindowClick(Tool,83,147)
        cycleCount-=1
    #双击快速布阵 刷新游戏中cd
    WindowClick(Tool,102,161)
    time.sleep(0.2)
    ToolPanelClick(102,161)


print("""
请输入数字:
1.启动游戏1
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

    #持续等待键盘按键
    def KeyboardWait(self):
        print("已开启阻塞 脚本保持运行")
        keyboard.wait()

def Init():
    print("""
    'Ctrl+1' 启动
    'Ctrl+2' 应总选卡 有等待加载
    'Ctrl+3' 点了个重新开始
    """)
    KeyboardEvent().KeyboardWait()

Init()