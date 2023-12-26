#自写脚本调用
import interactive_menu
from keyboard_event import *
import threading
    
def Init():
    print("""
    'Ctrl+1' 启动
    'Ctrl+2' 应总选卡 有等待加载
    'Ctrl+3' 点了个重新开始4        
    """) 
    keyboard_event = KeyboardEvent()
    threading.Thread(target=interactive_menu.main).start()
    keyboard_event.KeyboardWait()
Init()