#自写脚本调用
import interactive_menu
from keyboard_event import *
    
def Init():
    print("""
    'Ctrl+1' 启动
    'Ctrl+2' 应总选卡 有等待加载
    'Ctrl+3' 点了个重新开始4        
    """) 
    KeyboardEvent()
    interactive_menu.main()
    KeyboardEvent().KeyboardWait()
Init()