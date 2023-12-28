from pynput import keyboard
from interactive_menu import *
import threading

# 定义热键触发的函数
def on_activate_0():
    print('热键 Ctrl+0 被触发')
    threading.Thread(target=interactive_menu.main).start()
    

def on_activate_1():
    print('热键 Ctrl+1 被触发')

# ... 为每个热键定义一个函数

# 将函数放入列表
actions = [on_activate_0, on_activate_1]  # ... 添加所有的函数

# 创建热键对象列表
hotkeys = [
    keyboard.HotKey(
        [keyboard.Key.ctrl, keyboard.KeyCode.from_char(str(i))], 
        actions[i]  # 使用相应的函数作为回调函数
    ) 
    for i in range(len(actions))  # 注意这里的范围是函数列表的长度
]

# 定义键盘事件的处理函数
def for_canonical(f):
    return lambda k: f(listener.canonical(k))

hotkeys = {hk: for_canonical(hk) for hk in hotkeys}

# 定义键盘监听事件
def on_press(key):
    for hotkey in hotkeys:
        if hotkey.press(key):
            break

def on_release(key):
    for hotkey in hotkeys:
        if hotkey.release(key):
            break

# 创建并启动键盘监听
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()