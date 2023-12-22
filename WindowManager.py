import time
import win32gui
import win32con
import subprocess
import os
from CommonData import *

#置顶窗口
def TopWindow(object):
    if object.hwnd:
        win32gui.ShowWindow(object.hwnd, win32con.SW_SHOWNORMAL)
        print("成功置顶窗口", object.name)
    else:
        print("无法置顶窗口", object.name)
        exit(1)

#关闭窗口
def CloseWindow(object):
    if object.hwnd:
        win32gui.PostMessage(object.hwnd, win32con.WM_CLOSE, 0, 0)
        object.ClearData()
        print("成功关闭窗口", object.name)
    else:
        print("无法关闭窗口", object.name)
        exit(1)

#打开程序
def OpenWindow(object):
    try:
        subprocess.Popen(object.path, cwd = os.path.dirname(object.path))
        print("成功打开窗口", object.name)
    except:
        print("无法打开窗口", object.name)
        exit(1)
    #sleep以下不然无法获取到窗口
    time.sleep(0.2)
    temphwnd = win32gui.FindWindow(None, object.name)
    while(temphwnd == 0):#持续获取 除非你瞬间自己关闭 或者游戏窗口名字有问题否则不会死循环
        time.sleep(0.1)
        temphwnd = win32gui.FindWindow(None, object.name)
    object.hwnd = temphwnd
    if object == Tool:
        object.hwnd = temphwnd
        print(temphwnd)
        #获取窗口四角点位
        object.left, object.top, object.right, object.bottom = win32gui.GetWindowRect(object.hwnd)
        print("成功获取Tool窗口坐标" )

#检查窗口是否开启
def CheckWindowIsOpen(object):
    temphwnd = win32gui.FindWindow(None, object.name)
    if temphwnd == 0:
        print("窗口未开启", object.name)
        return False
    else:
        object.hwnd = temphwnd
        time.sleep( 0.5)
        print("窗口已开启", object.name)
        return True